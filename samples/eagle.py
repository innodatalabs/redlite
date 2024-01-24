import os
from redlite import run, load_dataset
from redlite.hf.hf_model import HFModel
from redlite.metric import PrefixMetric


model = HFModel("cookinai/Bald-Eagle-7B", token=os.environ["HF_TOKEN"], max_length=2048)
dataset = load_dataset("hf:innodatalabs/rt-gsm8k")
metric = PrefixMetric(ignore_case=True, ignore_punct=True, strip=True)

run(model=model, dataset=dataset, metric=metric)
