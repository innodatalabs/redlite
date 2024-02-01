from redlite.util import format_duration, parse_duration


def test_parse_duration():
    assert parse_duration("1.5s") == 1.5
    assert parse_duration("2m 33.5s") == 120 + 33.5
    assert parse_duration("1h") == 60 * 60
    assert parse_duration("1d") == 60 * 60 * 24


def test_format_duration():
    assert format_duration(60 * 60 * 24) == "1d 0h 0m 0s"


def test_format_duration_float():
    assert format_duration(60 * 60 * 24.0) == "1d 0h 0m 0.0s"


def test_parse_duration_float():
    assert parse_duration("1d 0h 0m 0.0s") == 60 * 60 * 24.0
