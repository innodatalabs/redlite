from redlite import run
from redlite.benchmark.math500 import metric, dataset
from redlite.model.openai_model import OpenAIModel
import os

model = OpenAIModel(model="gpt-4o", api_key=os.environ["OPENAI_API_KEY"])

run(model=model, dataset=dataset, metric=metric)
