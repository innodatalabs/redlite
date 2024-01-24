import os
from redlite import run
from redlite.hf import HFDataset
from redlite.openai import OpenAIModel
from redlite.metric import PrefixMetric


model = OpenAIModel(api_key=os.environ["OPENAI_API_KEY"])

dataset = HFDataset("innodatalabs/rt-gaia")
metric = PrefixMetric(ignore_case=True, ignore_punct=True, strip=True)

run(model=model, dataset=dataset, metric=metric)
