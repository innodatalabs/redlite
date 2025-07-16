import os
from redlite import run, load_dataset
from redlite.model.hf_model import HFModel
from redlite.model import IgnoreSystemModel
from redlite.metric import MatchMetric
import torch

model = IgnoreSystemModel(HFModel(
    "google/gemma-3-4b-it",
    max_length=8192,
    task='image-text-to-text',
    token=os.environ["HF_TOKEN"],
    truncation=True,
    device_map='cuda:0',
    torch_dtype=torch.bfloat16,
))

dataset = load_dataset("hf:innodatalabs/rt-cogensumm")
metric = MatchMetric(ignore_case=True, ignore_punct=True, strategy='prefix')

run(model=model, dataset=dataset, metric=metric)
