import json

from .._core import NamedModel, Message, MissingDependencyError, log
from .._util import sha_digest
from typing import Any

try:
    import boto3
except ImportError as err:
    raise MissingDependencyError("Please install boto3 library") from err


class AwsBedrockModel(NamedModel):
    """
    Text generation models from AWS Bedrock.

    - **model_id** (`str`): identifier of the AWS Bedrock model, e.g. `"amazon.titan-text-agile-v1"`.
    - **aws_access_key_id** (`str | None`): AWS access key id
    - **aws_secret_access_key** (`str | None`): AWS secret access key
    - **region_name** (`str | None`): AWS region (optional).
    - **endpoint_uri** (`str | None`): AWS endpoint (optional).
    - **text_generation_config** (`dict | None`): optional configuration,
        see [AWS docs](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-parameters.html).
    """

    def __init__(
        self,
        model_id: str,
        aws_access_key_id: str | None = None,
        aws_secret_access_key: str | None = None,
        region_name: str | None = None,
        endpoint_url: str | None = None,
        text_generation_config: dict[str, Any] | None = None,
    ):
        self.client = boto3.client(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            service_name="bedrock-runtime",
            region_name=region_name,
            endpoint_url=endpoint_url,
        )
        self.text_generation_config = text_generation_config
        self.model_id = model_id

        name = "aws-bedrock-" + model_id
        if text_generation_config is not None:
            name += "@" + sha_digest(text_generation_config)

        super().__init__(name, self.__predict)

    def __predict(self, messages: list[Message]) -> str:
        prompt = _apply_chat_template(messages)
        data: dict[str, Any] = {
            "inputText": prompt,
        }
        if self.text_generation_config is not None:
            data["textGenerationConfig"] = self.text_generation_config

        response = self.client.invoke_model(
            body=json.dumps(data).encode("utf-8"),
            modelId=self.model_id,
            accept="application/json",
            contentType="application/json",
        )
        response_body = json.loads(response.get("body").read())

        finish_reason = response_body.get("error")
        if finish_reason is not None:
            raise RuntimeError(f"Bedrock text generation error: {finish_reason}")

        assert len(response_body["results"]) == 1
        if response_body["results"][0]["completionReason"] != "FINISH":
            log.warning(f'generation completed with status {response_body["results"][0]["completionReason"]}')
        return response_body["results"][0]["outputText"]


def _apply_chat_template(messages: list[Message]) -> str:
    if messages[0]["role"] == "system":
        return "System: " + messages[0]["content"] + "\n" + _apply_chat_template(messages[1:])
    assert messages[0]["role"] == "user"
    assert len(messages) % 2 == 1

    out = []
    for i in range(0, len(messages) - 1, 2):
        out.append("User: " + messages[i]["content"] + "\n")
        out.append("Bot: " + messages[i + 1]["content"] + "\n")
    out.append("User: " + messages[-1]["content"] + "\nBot:")

    return "".join(out)
