import os
from redlite import run, load_dataset
from redlite.model.openai_model import OpenAIModel
from redlite.metric import MatchMetric


model = OpenAIModel(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ["NGC_API_KEY"],
    model="meta/llama3-8b-instruct",
    temperature=0.5,
    top_p=1,
    max_tokens=1024,
)
dataset = load_dataset("hf:innodatalabs/rt-gsm8k-gaia")
metric = MatchMetric(ignore_case=True, ignore_punct=True, strategy='prefix')

run(model=model, dataset=dataset, metric=metric)
