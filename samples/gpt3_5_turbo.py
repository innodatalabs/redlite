import os
from redlite import run, load_dataset
from redlite.model.openai_model import OpenAIModel
from redlite.metric import MatchMetric


model = OpenAIModel(api_key=os.environ["OPENAI_API_KEY"])
dataset = load_dataset("hf:innodatalabs/rt-gaia")
metric = MatchMetric(ignore_case=True, ignore_punct=True, strategy='prefix')

run(model=model, dataset=dataset, metric=metric)
