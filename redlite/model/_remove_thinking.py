import re
from .._core import NamedModel, Message


class RemoveThinking(NamedModel):
    """
    Wraps a model and removes system message from the model input (if any).
    Useful if underlying model was not trained with system message.

    - **model** (`NamedModel`): the model to wrap.
    """

    def __init__(self, model: NamedModel):
        self.model = model
        super().__init__(f"remove-thinking-{model.name}", self.__engine)

    def __engine(self, messages: list[Message]) -> str:
        return _remove_thinking_trace(self.__engine(messages))


_RE_THINKING_TRACE = {
    "openai-oss": r"<\|start\|>assistant<\|channel\|>final<\|message\|>(.*)<\|return\|>$",
    "<thinking>": r"</thinking>(.*)$",
}


def _remove_thinking_trace(content: str) -> str:
    for pattern in _RE_THINKING_TRACE.values():
        mtc = re.search(pattern, content, flags=re.DOTALL | re.IGNORECASE)
        if mtc is not None:
            return mtc.group(1).strip()
    print("Warning: could not remove thinking trace from content")
    return content
