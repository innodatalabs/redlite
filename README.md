# RedLite

An opinionated toolset for testing Language Models for safety.

## User experience

1. `pip install redlite[all]`
2. Generate several runs (using Python scripting, see below)
3. `redlite server --port <PORT>`

## Python API

```python
from redlite import run, NamedModel, Message
from redlite.hf import HFDataset
from redlite.metric import BleuMetric


def parrot(messages: list[Message]) -> str:
    return messages[-1].content


model = NamedModel("parrot", parrot)

dataset = HFDataset("innodatalabs/rt-cogensumm")
metric = BleuMetric()

run(model=model, dataset=dataset, metric=metric)
```

## Develop

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .[dev,all]
```

Make commands:

* test
* test-server
* lint
* wheen
* docs


## TODO

- [x] deps cleanup (randomname!)
- [ ] review/improve module structure
- [ ] automate CI/CD
- [ ] write docs
- [ ] publish docs automatically (CI/CD)
- [ ] web UI styling
- [ ] better test server
- [ ] tests
- [ ] Integrations (HF, OpenAI, Anthropic, vLLM)
- [ ] Fix data format in HF datasets (innodatalabs/rt-* ones) to match standard
- [ ] more robust backend API (future-proof)
- [ ] better error handling for missing deps
- [ ] document which deps we need when
