from redlite.metric.f1 import F1Metric


def test_smoke():
    m = F1Metric()

    assert m("Good day", "Good day") == 1.0
    assert m("Good day", "good day") == 1.0
    assert m("Good day", "the good day") == 1.0
    assert m("Good day", "the") == 0.0
