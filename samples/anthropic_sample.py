import os
from redlite import run, load_dataset
from redlite.model.anthropic_model import AnthropicModel
from redlite.metric import MatchMetric


model = AnthropicModel(
    api_key=os.environ["ANTHROPIC_API_KEY"],
    model='claude-sonnet-4-20250514',
    max_tokens=8000,
    thinking={'type': 'enabled', 'budget_tokens': 2000}
)
dataset = load_dataset("hf:innodatalabs/rt-cogensumm")
metric = MatchMetric(ignore_case=True, ignore_punct=True, strategy='prefix')

run(model=model, dataset=dataset, metric=metric, max_samples=10)
