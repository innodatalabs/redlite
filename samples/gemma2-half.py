import os
from redlite import run, load_dataset
from redlite.model.hf_model import HFModel
from redlite.model import IgnoreSystemModel
from redlite.metric import MatchMetric

from transformers import AutoModelForCausalLM, AutoTokenizer


engine = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2-9b-it",
    token=os.environ["HF_TOKEN"],
    device_map="cuda:0"
)
engine.half()
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-9b-it")

model = IgnoreSystemModel(HFModel(
    "google/gemma-2-9b-it",
    model=engine,
    tokenizer=tokenizer,
    max_length=8192,
    truncation=True,
    device_map='cuda:0',
))

dataset = load_dataset("hf:innodatalabs/rt-cogensumm")
metric = MatchMetric(ignore_case=True, ignore_punct=True, strategy='prefix')

run(model=model, dataset=dataset, metric=metric)

