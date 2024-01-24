from redlite import run, load_dataset, NamedModel, Messages
from redlite.metric import BleuMetric


def parrot(messages: Messages) -> str:
    return messages[-1]["content"] + " ho ho ho"


model = NamedModel("parrot", parrot)
dataset = load_dataset("hf:innodatalabs/rt-cogensumm")
metric = BleuMetric()

run(model=model, dataset=dataset, metric=metric)
