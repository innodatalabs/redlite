import os
from redlite import run, load_dataset
from redlite.hf.hf_model import HFModel
from redlite.metric import PrefixMetric


model = HFModel("mistralai/Mistral-7B-Instruct-v0.2", token=os.environ["HF_TOKEN"])
dataset = load_dataset("hf:innodatalabs/rt-gaia")
metric = PrefixMetric(ignore_case=True, ignore_punct=True, strip=True)

run(model=model, dataset=dataset, metric=metric)
