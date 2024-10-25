from redlite import run, load_dataset
from redlite.model import CannedModel, ThrottleModel
from redlite.metric import MatchMetric


model = ThrottleModel(CannedModel('I can not answer this question'), calls_per_minute=10)
dataset = load_dataset("hf:innodatalabs/rt-factcc")
metric = MatchMetric(ignore_case=True, ignore_punct=True, strategy='prefix')

run(model=model, dataset=dataset, metric=metric, max_samples=10)
