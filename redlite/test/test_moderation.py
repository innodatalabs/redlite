from redlite.model._moderation import ModerationModel
from unittest.mock import Mock


def test_moderation_model_name():
    """Verify name composition follows pattern"""
    inner_model = Mock()
    inner_model.name = "gpt-4"

    model = ModerationModel(inner_model, api_key="test-key")

    assert model.name == "moderated-gpt-4"


def test_moderation_passes_safe_content():
    """When content is safe, delegate to inner model"""
    inner_model = Mock()
    inner_model.name = "gpt-4"
    inner_model.return_value = "Safe response"

    model = ModerationModel(inner_model, api_key="test-key")

    # Mock OpenAI client
    mock_result = Mock(flagged=False)
    mock_moderation = Mock(results=[mock_result])
    model.client.moderations.create = Mock(return_value=mock_moderation)

    messages = [{"role": "user", "content": "What is the weather?"}]
    result = model(messages)

    assert result == "Safe response"
    inner_model.assert_called_once_with(messages)
    model.client.moderations.create.assert_called_once_with(
        model="omni-moderation-latest", input=["What is the weather?"]
    )


def test_moderation_blocks_flagged_content():
    """When content is flagged, return refusal message without calling inner model"""
    inner_model = Mock()
    inner_model.name = "gpt-4"

    model = ModerationModel(inner_model, api_key="test-key")

    # Mock flagged content
    mock_result = Mock(flagged=True)
    mock_moderation = Mock(results=[mock_result])
    model.client.moderations.create = Mock(return_value=mock_moderation)

    messages = [{"role": "user", "content": "Harmful content"}]
    result = model(messages)

    assert result == "I refuse to answer this question."
    inner_model.assert_not_called()


def test_moderation_custom_refusal_message():
    """Test custom refusal message"""
    inner_model = Mock()
    inner_model.name = "gpt-4"
    custom_message = "Content violates policy"

    model = ModerationModel(inner_model, api_key="test-key", refusal_message=custom_message)

    # Mock flagged content
    mock_result = Mock(flagged=True)
    mock_moderation = Mock(results=[mock_result])
    model.client.moderations.create = Mock(return_value=mock_moderation)

    result = model([{"role": "user", "content": "test"}])
    assert result == custom_message


def test_moderation_multiple_messages():
    """Test that all messages are checked"""
    inner_model = Mock()
    inner_model.name = "gpt-4"
    inner_model.return_value = "Response"

    model = ModerationModel(inner_model, api_key="test-key")

    # Mock all safe
    mock_results = [Mock(flagged=False), Mock(flagged=False), Mock(flagged=False)]
    mock_moderation = Mock(results=mock_results)
    model.client.moderations.create = Mock(return_value=mock_moderation)

    messages = [
        {"role": "system", "content": "You are helpful"},
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there"},
    ]

    model(messages)

    # Should extract all contents
    model.client.moderations.create.assert_called_once_with(
        model="omni-moderation-latest", input=["You are helpful", "Hello", "Hi there"]
    )


def test_moderation_api_error_fails_closed():
    """Test that API errors result in refusal (fail-closed behavior)"""
    inner_model = Mock()
    inner_model.name = "gpt-4"

    model = ModerationModel(inner_model, api_key="test-key")

    # Mock API error
    model.client.moderations.create = Mock(side_effect=Exception("API Error"))

    messages = [{"role": "user", "content": "test"}]
    result = model(messages)

    # Should return refusal, not call inner model
    assert result == "I refuse to answer this question."
    inner_model.assert_not_called()
