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


def test_against_helm():
    m = RougeMetric(rouge_type="rouge2")

    expected = "N/A"
    actual = """N/A

The summary sentences are consistent with the information provided in the article. However, it's important \
to note that the article states that "Hearn insisted he has not demanded rights to promote Frampton’s future \
fights," but the summary does not include this detail. However, this is not a contradiction or an incorrect \
statement, as the summary does not make any claims about future promotional rights.
"""

    assert m(expected, actual) == 0.029411764705882353
