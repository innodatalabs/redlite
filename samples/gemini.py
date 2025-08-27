import os
from redlite import run, load_dataset
from redlite.model.gemini_model import GeminiModel
from redlite.metric import MatchMetric


model = GeminiModel(api_key=os.environ["GOOGLE_GEMINI_API_KEY"])
dataset = load_dataset("hf:innodatalabs/rt-cogensumm")
metric = MatchMetric(ignore_case=True, ignore_punct=True, strategy='prefix')

run(model=model, dataset=dataset, metric=metric, max_samples=10)
