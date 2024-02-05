from redlite.metric.rouge import RougeMetric, RougeCJKMetric


def test_smoke():
    m = RougeMetric(rouge_type="rouge1")

    assert m("Good day", "Good day") == 1.0
    assert m("Good day", "good day") == 1.0
    assert m("Good day", "Good blah day") == 0.8


def test_cjk_smoke():
    m = RougeCJKMetric(rouge_type="rouge1")

    assert m("Good day", "Good day") == 1.0
    assert m("Good day", "good day") == 0.875
    assert m("Good day", "Good blah day") == 0.761904761904762
