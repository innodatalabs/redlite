import os
from redlite import run, load_dataset
from redlite.model.hf_model import HFModel
from redlite.metric import MatchMetric


model = HFModel("meta-llama/Meta-Llama-3-8B-Instruct", token=os.environ["HF_TOKEN"], max_length=8192)
dataset = load_dataset("hf:innodatalabs/rt-cogensumm")
metric = MatchMetric(ignore_case=True, ignore_punct=True, strategy='prefix')

run(model=model, dataset=dataset, metric=metric)
