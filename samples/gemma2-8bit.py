import os
from redlite import run, load_dataset
from redlite.model.hf_model import HFModel
from redlite.model import IgnoreSystemModel
from redlite.metric import MatchMetric

from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(
    load_in_8bit=True,
    llm_int8_threshold=200.0
)

engine = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2-9b-it",
    token=os.environ["HF_TOKEN"],
    quantization_config=quantization_config,
    device_map="cuda:0"
)
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-9b-it")

model = IgnoreSystemModel(HFModel("google/gemma-2-9b-it",
    model=engine, tokenizer=tokenizer, truncation=True, max_length=8192, device_map='cuda:0'))

dataset = load_dataset("hf:innodatalabs/rt-cogensumm")
metric = MatchMetric(ignore_case=True, ignore_punct=True, strategy='prefix')

run(model=model, dataset=dataset, metric=metric)

