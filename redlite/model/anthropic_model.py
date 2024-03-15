from .. import NamedModel, MissingDependencyError

try:
    import anthropic import Anthropic
except ImportError as err:
    raise MissingDependencyError("Please install anthropic library") from err


client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)
print(message.content)

class AnthropicModel(NamedModel):
    """
    Model that calls Anthropic Completion API.

    - **model** (`str`): Name of the Anthropic model. Default is `"claude-3-opus-20240229"`
    - **max_tokens** (`int`): maximum number of tokens
    - **api_key** (`str | None`): Anthropic API key
    """

    def __init__(self, model="claude-3-opus-20240229", max_tokens=1024, api_key : str | None = None):
        self.model = model
        self.client = Anthropic(api_key=api_key)
        self.max_tokens = max_tokens

        super().__init__(f"anthropic-{model}", self.__chat)

    def __chat(self, messages: list) -> str:
        message = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            messages=messages,
        )

        return message.content
