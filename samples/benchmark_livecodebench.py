from redlite import run, rescore
from redlite.benchmark.livecodebench import get_dataset, get_metric
from redlite.model.openai_model import OpenAIModel
import os


# model = OpenAIModel(model="o4-mini", api_key=os.environ["OPENAI_API_KEY"])

# dataset = get_dataset()

metric = get_metric()

# run(model=model, dataset=dataset, metric=metric)
rescore(run='cool-staff-290', metric=metric)
