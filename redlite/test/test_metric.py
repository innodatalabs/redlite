from redlite.metric import MatchMetric


def test_prefix_smoke():
    m = MatchMetric(strategy="prefix")

    assert m("Good", "Good") == 1.0
    assert m("Good", "good") == 0.0
    assert m("Good", "Good blah") == 1.0


def test_exact_smoke():
    m = MatchMetric()

    assert m("Good", "Good") == 1.0
    assert m("Good", "good") == 0.0
    assert m("Good", "Good blah") == 0.0


def test_substring_smoke():
    m = MatchMetric(strategy="contains")

    assert m("Good", "Good") == 1.0
    assert m("Good", "good") == 0.0
    assert m("Good", "Good blah") == 1.0
    assert m("Good", "blah Good") == 1.0


def test_prefix_ignore_case():
    m = MatchMetric(strategy="prefix", ignore_case=True)

    assert m("Good", "Good") == 1.0
    assert m("Good", "good") == 1.0
    assert m("Good", "GOOD blah") == 1.0


def test_exact_ignore_case():
    m = MatchMetric(ignore_case=True)

    assert m("Good", "Good") == 1.0
    assert m("Good", "good") == 1.0
    assert m("Good", "GOOD blah") == 0.0


def test_prefix_ignore_punct():
    m = MatchMetric(ignore_punct=True, strategy="prefix")

    assert m("Good.", "Good") == 1.0
    assert m("Good", "[Good]") == 1.0
    assert m("Good", "[good]") == 0.0
    assert m("Good", "GOOD blah") == 0.0


def test_exact_ignore_punct():
    m = MatchMetric(ignore_punct=True)

    assert m("Good.", "Good") == 1.0
    assert m("Good", "[Good]") == 1.0
    assert m("Good", "[good]") == 0.0
    assert m("Good", "GOOD blah") == 0.0


def test_prefix_normalize_whitespace():
    m = MatchMetric(strategy="prefix")

    assert m("Good.", "Good") == 0.0
    assert m("Good", " Good ") == 1.0
    assert m("Very Good", " Very\n\nGood ") == 1.0
    assert m("Very Good", " Very\n\ngood ") == 0.0
    assert m("Very Good", " Very\n\nGood\nBlah") == 1.0
    assert m("Very Good", " Very\n\ngood\nBlah") == 0.0


def test_exact_normalize_whitespace():
    m = MatchMetric()

    assert m("Good.", "Good") == 0.0
    assert m("Good", " Good ") == 1.0
    assert m("Very Good", " Very\n\nGood ") == 1.0
    assert m("Very Good", " Very\n\ngood ") == 0.0
    assert m("Very Good", " Very\n\nGood\nBlah") == 0.0
    assert m("Very Good", " Very\n\ngood\nBlah") == 0.0


def test_contains_fullword():
    m = MatchMetric(strategy="contains")

    assert m("correct", "incorrect") == 0.0
    assert m("correct", "may be correct or incorrect") == 1.0
