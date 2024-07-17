from .. import NamedModel, MissingDependencyError
from .._util import object_digest

try:
    from openai import OpenAI, NOT_GIVEN
except ImportError as err:
    raise MissingDependencyError("Please install openai library") from err


class OpenAIModel(NamedModel):
    """
    Model that calls OpenAI Completion API.

    - **base_url** (`str`): Alternative API endpoint. Can be used to access services that
                            are compatible with OpenAI (e.g. NVIDIA research).
    - **model** (`str`): Name of the OpenAI model. Default is `"gpt-3.5-turbo"`.
    - **max_tokens** (`int`): Maximum number of returned tokens.
    - **temperature** (`float`): Generation temperature, in the range 0-1.
    - **top_p** (`int`): Number of "top P" samples for generation.
    - **api_key** (`str`): OpenAI API key
    - **max_retries** (`int`): How many times to retry a failed request. Default is `2`.
    """

    def __init__(
        self,
        *,
        model="gpt-3.5-turbo",
        base_url=None,
        max_tokens=NOT_GIVEN,
        temperature=NOT_GIVEN,
        top_p=NOT_GIVEN,
        api_key=None,
        max_retries=2,
    ):
        self.base_url = base_url
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.client = OpenAI(api_key=api_key, max_retries=max_retries, base_url=base_url)

        signature = {}
        if base_url is not None:
            signature["base_url"] = base_url
        if max_tokens is not NOT_GIVEN:
            signature["max_tokens"] = max_tokens
        if temperature is not NOT_GIVEN:
            signature["temperature"] = temperature
        if top_p is not NOT_GIVEN:
            signature["top_p"] = top_p

        name = "openai"
        if len(signature) > 0:
            name = f"openai-{object_digest(signature)[:6]}"

        super().__init__(f"{name}-{model}", self.__chat)

    def __chat(self, messages: list) -> str:
        chat_completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            top_p=self.top_p,
        )

        return chat_completion.choices[0].message.content
