from redlite.metric.bleu import BleuMetric, BleuCJKMetric
import nltk
nltk.download('punkt')

def test_smoke():
    m = BleuMetric()

    assert m("Good day", "Good day") == 1.0
    assert m("Good day", "good day") == 0.5
    assert m("Good day", "Good blah day") == 0.6666666666666666


def test_cjk_smoke():
    m = BleuCJKMetric()

    assert m("Good day", "Good day") == 1.0
    assert m("Good day", "good day") == 0.875
    assert m("Good day", "Good blah day") == 0.6153846153846154
