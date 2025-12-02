from redlite.model.openai_model import OpenAIModel
from unittest.mock import Mock, patch


def test_openai_model_with_safety_identifier():
    """Test that safety_identifier is passed to OpenAI API"""
    with patch("redlite.model.openai_model.OpenAI") as MockOpenAI:
        # Setup mock client
        mock_client = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Test response"
        mock_client.chat.completions.create.return_value = mock_response
        MockOpenAI.return_value = mock_client

        # Create model with safety_identifier
        model = OpenAIModel(
            model="gpt-4",
            api_key="test-key",
            safety_identifier="user_123456"
        )

        # Verify safety_identifier is in params
        assert "safety_identifier" in model.params
        assert model.params["safety_identifier"] == "user_123456"

        # Call the model
        messages = [{"role": "user", "content": "Hello"}]
        result = model(messages)

        # Verify safety_identifier was passed to API
        mock_client.chat.completions.create.assert_called_once()
        call_kwargs = mock_client.chat.completions.create.call_args[1]
        assert call_kwargs["safety_identifier"] == "user_123456"
        assert result == "Test response"


def test_openai_model_without_safety_identifier():
    """Test that model works normally without safety_identifier"""
    with patch("redlite.model.openai_model.OpenAI") as MockOpenAI:
        # Setup mock client
        mock_client = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Test response"
        mock_client.chat.completions.create.return_value = mock_response
        MockOpenAI.return_value = mock_client

        # Create model without safety_identifier
        model = OpenAIModel(model="gpt-4", api_key="test-key")

        # Verify safety_identifier is not in params
        assert "safety_identifier" not in model.params

        # Call the model
        messages = [{"role": "user", "content": "Hello"}]
        result = model(messages)

        # Verify safety_identifier was not passed to API
        mock_client.chat.completions.create.assert_called_once()
        call_kwargs = mock_client.chat.completions.create.call_args[1]
        assert "safety_identifier" not in call_kwargs
        assert result == "Test response"


def test_openai_model_name_includes_safety_identifier():
    """Test that model name includes safety_identifier in signature"""
    with patch("redlite.model.openai_model.OpenAI"):
        model1 = OpenAIModel(model="gpt-4", api_key="test-key")
        model2 = OpenAIModel(
            model="gpt-4",
            api_key="test-key",
            safety_identifier="user_123456"
        )

        # Models with different safety_identifiers should have different names
        assert model1.name != model2.name
        assert "gpt-4" in model1.name
        assert "gpt-4" in model2.name
