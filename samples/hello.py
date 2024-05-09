from redlite import run, load_dataset, NamedModel, Message
from redlite.metric.bleu import BleuMetric


def parrot(messages: list[Message]) -> str:
    return messages[-1]["content"] + " ho ho ho"


model = NamedModel("parrot", parrot)
dataset = load_dataset("hf:innodatalabs/rt-inod-jailbreaking")
metric = BleuMetric()

run(model=model, dataset=dataset, metric=metric, max_samples=250)
