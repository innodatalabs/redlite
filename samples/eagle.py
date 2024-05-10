import os
from redlite import run, load_dataset
from redlite.model.hf_model import HFModel
from redlite.metric import MatchMetric


model = HFModel("cookinai/Bald-Eagle-7B", token=os.environ["HF_TOKEN"])
dataset = load_dataset("hf:innodatalabs/rt-cogensumm")
metric = MatchMetric(ignore_case=True, ignore_punct=True, strategy='prefix')

run(model=model, dataset=dataset, metric=metric)
