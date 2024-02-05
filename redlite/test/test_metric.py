from redlite.metric import PrefixMetric, ExactMetric


def test_prefix_smoke():
    m = PrefixMetric()

    assert m("Good", "Good") == 1.0
    assert m("Good", "good") == 0.0
    assert m("Good", "Good blah") == 1.0


def test_exact_smoke():
    m = ExactMetric()

    assert m("Good", "Good") == 1.0
    assert m("Good", "good") == 0.0
    assert m("Good", "Good blah") == 0.0


def test_prefix_ignore_case():
    m = PrefixMetric(ignore_case=True)

    assert m("Good", "Good") == 1.0
    assert m("Good", "good") == 1.0
    assert m("Good", "GOOD blah") == 1.0


def test_exact_ignore_case():
    m = ExactMetric(ignore_case=True)

    assert m("Good", "Good") == 1.0
    assert m("Good", "good") == 1.0
    assert m("Good", "GOOD blah") == 0.0


def test_prefix_ignore_punct():
    m = PrefixMetric(ignore_punct=True)

    assert m("Good.", "Good") == 1.0
    assert m("Good", "[Good]") == 1.0
    assert m("Good", "[good]") == 0.0
    assert m("Good", "GOOD blah") == 0.0


def test_exact_ignore_punct():
    m = ExactMetric(ignore_punct=True)

    assert m("Good.", "Good") == 1.0
    assert m("Good", "[Good]") == 1.0
    assert m("Good", "[good]") == 0.0
    assert m("Good", "GOOD blah") == 0.0


def test_prefix_normalize_whitespace():
    m = PrefixMetric(normalize_whitespace=True)

    assert m("Good.", "Good") == 0.0
    assert m("Good", " Good ") == 1.0
    assert m("Very Good", " Very\n\nGood ") == 1.0
    assert m("Very Good", " Very\n\ngood ") == 0.0
    assert m("Very Good", " Very\n\nGood\nBlah") == 1.0
    assert m("Very Good", " Very\n\ngood\nBlah") == 0.0


def test_exact_normalize_whitespace():
    m = ExactMetric(normalize_whitespace=True)

    assert m("Good.", "Good") == 0.0
    assert m("Good", " Good ") == 1.0
    assert m("Very Good", " Very\n\nGood ") == 1.0
    assert m("Very Good", " Very\n\ngood ") == 0.0
    assert m("Very Good", " Very\n\nGood\nBlah") == 0.0
    assert m("Very Good", " Very\n\ngood\nBlah") == 0.0
