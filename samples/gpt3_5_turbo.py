import os
from redlite import run, load_dataset
from redlite.openai import OpenAIModel
from redlite.metric import PrefixMetric


model = OpenAIModel(api_key=os.environ["OPENAI_API_KEY"])
dataset = load_dataset("hf:innodatalabs/rt-gaia")
metric = PrefixMetric(ignore_case=True, ignore_punct=True, strip=True)

run(model=model, dataset=dataset, metric=metric)
