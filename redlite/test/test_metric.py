from redlite.metric import PrefixMetric


def test_smoke():
    m = PrefixMetric()

    assert m("Good", "Good") == 1.0
    assert m("Good", "good") == 0.0
    assert m("Good", "Good blah") == 1.0


def test_ignore_case():
    m = PrefixMetric(ignore_case=True)

    assert m("Good", "Good") == 1.0
    assert m("Good", "good") == 1.0
    assert m("Good", "GOOD blah") == 1.0


def test_ignore_punct():
    m = PrefixMetric(ignore_punct=True)

    assert m("Good.", "Good") == 1.0
    assert m("Good", "[Good]") == 1.0
    assert m("Good", "[good]") == 0.0
    assert m("Good", "GOOD blah") == 0.0
