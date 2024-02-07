import os
from redlite import run, load_dataset
from redlite.model.hf_model import HFModel
from redlite.metric import PrefixMetric


model = HFModel("openchat/openchat-3.5-0106", token=os.environ["HF_TOKEN"], max_length=8192)
dataset = load_dataset("innodatalabs/rt-factcc")
metric = PrefixMetric(ignore_case=True, ignore_punct=True, strip=True)

run(model=model, dataset=dataset, metric=metric)
