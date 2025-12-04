from redlite.model import IgnoreSystemModel, ConvertSystemToUserModel, RemoveThinking
from unittest.mock import Mock


def test_ignore_system_model():
    engine_model = Mock()
    engine_model.name = "engine"

    model = IgnoreSystemModel(engine_model)
    model(
        [
            {"role": "system", "content": "SYS"},
            {"role": "user", "content": "USR"},
        ]
    )

    assert model.name == "ignore-system-engine"
    engine_model.assert_called_once_with(
        [
            {"role": "user", "content": "USR"},
        ]
    )


def test_convert_system_to_user_model():
    engine_model = Mock()
    engine_model.name = "engine"

    model = ConvertSystemToUserModel(engine_model)
    model(
        [
            {"role": "system", "content": "SYS"},
            {"role": "user", "content": "USR"},
        ]
    )

    assert model.name == "convert-system-engine"
    engine_model.assert_called_once_with(
        [
            {"role": "user", "content": "SYS"},
            {"role": "assistant", "content": "OK"},
            {"role": "user", "content": "USR"},
        ]
    )


def test_convert_system_to_user_model_with_custom_confirmation():
    engine_model = Mock()
    engine_model.name = "engine"

    model = ConvertSystemToUserModel(engine_model, "Aye aye, Sir!")
    model(
        [
            {"role": "system", "content": "SYS"},
            {"role": "user", "content": "USR"},
        ]
    )

    assert model.name == "convert-system-engine@78b18e"
    engine_model.assert_called_once_with(
        [
            {"role": "user", "content": "SYS"},
            {"role": "assistant", "content": "Aye aye, Sir!"},
            {"role": "user", "content": "USR"},
        ]
    )


def test_remove_thinking_model():
    engine_model = Mock()
    engine_model.name = "engine"
    engine_model.return_value = "Thinking hard...<|start|>assistant<|channel|>final<|message|>\
This is the answer.<|return|>"

    model = RemoveThinking(engine_model)
    response = model(
        [
            {"role": "user", "content": "What is 2+2?"},
        ]
    )

    assert model.name == "remove-thinking-engine"
    engine_model.assert_called_once_with(
        [
            {"role": "user", "content": "What is 2+2?"},
        ]
    )
    assert response == "This is the answer."


def test_remove_thinking_model_2():
    engine_model = Mock()
    engine_model.name = "engine"
    engine_model.return_value = "<thinking>Here I think hard</thinking>This is the answer."

    model = RemoveThinking(engine_model)
    response = model(
        [
            {"role": "user", "content": "What is 2+2?"},
        ]
    )

    assert model.name == "remove-thinking-engine"
    engine_model.assert_called_once_with(
        [
            {"role": "user", "content": "What is 2+2?"},
        ]
    )
    assert response == "This is the answer."


def test_remove_thinking_model_no_trace():
    engine_model = Mock()
    engine_model.name = "engine"
    engine_model.return_value = "This is the answer without thinking trace."

    model = RemoveThinking(engine_model)
    response = model(
        [
            {"role": "user", "content": "What is 2+2?"},
        ]
    )

    assert model.name == "remove-thinking-engine"
    engine_model.assert_called_once_with(
        [
            {"role": "user", "content": "What is 2+2?"},
        ]
    )
    assert response == "This is the answer without thinking trace."
