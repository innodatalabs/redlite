from redlite import run, NamedModel, Message
from redlite.hf import HFDataset
from redlite.metric import BleuMetric


def parrot(messages: list[Message]) -> str:
    return messages[-1].content + "ho ho ho"


model = NamedModel("parrot", parrot)

dataset = HFDataset("innodatalabs/rt-cogensumm")
metric = BleuMetric()

run(model=model, dataset=dataset, metric=metric)
