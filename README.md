# RedLite

An opinionated toolset for testing Conversational Language Models.

## Usage

1. Install required dependencies

    ```bash
    pip install redlite[all]
    ```

2. Generate several runs (using Python scripting, see [examples](samples/), and below)

3. Review and compare runs

    ```bash
    redlite server --port <PORT>
    ```

## Python API

```python
import os
from redlite import run, load_dataset
from redlite.openai import OpenAIModel
from redlite.metric import PrefixMetric


model = OpenAIModel(api_key=os.environ["OPENAI_API_KEY"])
dataset = load_dataset("hf:innodatalabs/rt-gaia")
metric = PrefixMetric(ignore_case=True, ignore_punct=True, strip=True)

run(model=model, dataset=dataset, metric=metric)
```

## Goals

* simple, easy-to-learn API
* lightweight
* only necessary dependencies
* framework-agnostic (PyTorch, Tensorflow, Keras, Flax, Jax)
* basic analytic tools included

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
* wheel
* docs
* black

## TODO

- [x] deps cleanup (randomname!)
- [ ] review/improve module structure
- [ ] automate CI/CD
- [ ] write docs
- [ ] publish docs automatically (CI/CD)
- [x] web UI styling
- [ ] better test server
- [ ] tests
- [ ] Integrations (HF, OpenAI, Anthropic, vLLM)
- [x] Fix data format in HF datasets (innodatalabs/rt-* ones) to match standard
- [ ] more robust backend API (future-proof)
- [ ] better error handling for missing deps
- [ ] document which deps we need when
- [ ] export to CSV
- [x] Upload to Zeno
