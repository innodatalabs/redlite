from redlite import run, NamedModel, Messages
from redlite.hf import HFDataset
from redlite.metric import BleuMetric


def parrot(messages: Messages) -> str:
    return messages[-1]["content"] + " ho ho ho"


model = NamedModel("parrot3", parrot)

dataset = HFDataset("innodatalabs/rt-cogensumm")
metric = BleuMetric()

run(model=model, dataset=dataset, metric=metric)
