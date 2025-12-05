from redlite import parallel_run, load_dataset, NamedModel, Message
from redlite.metric.bleu import BleuMetric
import time


def parrot(messages: list[Message]) -> str:
    time.sleep(1)
    return messages[-1]["content"] + " ho ho ho"


model_producer = lambda: NamedModel("parrot", parrot)
dataset = load_dataset("hf:innodatalabs/rt-cogensumm")
metric_producer = lambda: BleuMetric()

parallel_run(model_producer=model_producer, dataset=dataset, metric_producer=metric_producer, num_workers=4)
