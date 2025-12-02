from .._core import NamedModel, Message, MissingDependencyError, log

try:
    from openai import OpenAI
except ImportError as err:
    raise MissingDependencyError("Please install openai library") from err


class ModerationModel(NamedModel):
    """
    Wraps a model and filters conversation content using OpenAI Moderation API.

    https://platform.openai.com/docs/guides/safety-best-practices#use-our-free-moderation-api

    Before delegating to the inner model, all message contents are checked
    against OpenAI's moderation API. If any content is flagged as potentially
    harmful, the model returns a refusal message instead of processing the request.

    This avoids having OpenAI account flagged for Usage Policy Violation

    Requires OpenAI API key (via `api_key` parameter or OPENAI_API_KEY env var).

    - **model** (`NamedModel`): The model to wrap.
    - **api_key** (`str | None`): OpenAI API key. Optional, defaults to None
        (will use OPENAI_API_KEY environment variable).
    - **moderation_model** (`str`): Which OpenAI moderation model to use.
        Default is `"omni-moderation-latest"`.
    - **refusal_message** (`str`): Message to return when content is flagged.
        Default is `"I refuse to answer this question."`.
    - **safety_identifier** (`str | None`): Safety identifier to help OpenAI monitor
        and detect abuse. Should be a unique string per user (e.g., hashed username).
        Optional, defaults to None.

    Example:
    ```python
    from redlite.model import ModerationModel
    from redlite.model.openai_model import OpenAIModel

    # Create base model
    base_model = OpenAIModel(model="gpt-4")

    # Wrap with moderation and safety identifier
    safe_model = ModerationModel(base_model, safety_identifier="user_123456")

    # Safe content passes through
    response = safe_model([{"role": "user", "content": "What is Python?"}])

    # Harmful content is blocked
    response = safe_model([{"role": "user", "content": "harmful request"}])
    # Returns: "I refuse to answer this question."
    ```

    Note: If moderation API fails (network error, rate limit, etc.), the model
    will refuse to answer (fail-closed behavior) to maintain safety guarantees.
    """

    def __init__(
        self,
        model: NamedModel,
        *,
        api_key: str | None = None,
        moderation_model: str = "omni-moderation-latest",
        refusal_message: str = "I refuse to answer this question.",
        safety_identifier: str | None = None,
    ):
        self.model = model
        self.client = OpenAI(api_key=api_key)
        self.moderation_model = moderation_model
        self.refusal_message = refusal_message
        self.safety_identifier = safety_identifier
        super().__init__(f"moderated-{model.name}", self.__engine)

    def __engine(self, messages: list[Message]) -> str:
        # Extract content from all messages (remove roles)
        content_list = [msg["content"] for msg in messages]

        try:
            # Call OpenAI Moderation API
            moderation = self.client.moderations.create(
                model=self.moderation_model,
                input=content_list,
            )

            # Check if any content was flagged
            if any(result.flagged for result in moderation.results):
                return self.refusal_message

            # Content is safe, delegate to inner model
            # If safety_identifier is set and inner model supports it, inject it
            if self.safety_identifier and hasattr(self.model, 'params') and isinstance(self.model.params, dict):
                original_params = self.model.params.copy()
                self.model.params['safety_identifier'] = self.safety_identifier
                try:
                    result = self.model(messages)
                finally:
                    self.model.params = original_params
                return result
            else:
                return self.model(messages)

        except Exception as e:
            # Fail closed: if moderation API fails, refuse to answer
            log.warning(f"Moderation API error: {e}")
            return self.refusal_message
