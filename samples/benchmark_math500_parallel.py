from redlite import parallel_run
from redlite.benchmark.math500 import metric, dataset
from redlite.model.openai_model import OpenAIModel
import os

api_key = os.environ["OPENAI_API_KEY"]

model_producer = lambda: OpenAIModel(model="gpt-4o", api_key=api_key)
metric_producer = lambda: metric

parallel_run(model_producer=model_producer, dataset=dataset, metric_producer=metric_producer)
