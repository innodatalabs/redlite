import os
from redlite import run, load_dataset
from redlite.model.hf_model import HFModel
from redlite.metric import MatchMetric


model = HFModel("openchat/openchat-3.5-0106", token=os.environ["HF_TOKEN"], device_map='auto')
dataset = load_dataset("innodatalabs/rt-factcc")
metric = MatchMetric(ignore_case=True, ignore_punct=True, strategy='prefix')

run(model=model, dataset=dataset, metric=metric)
