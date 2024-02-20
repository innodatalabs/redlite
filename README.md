# RedLite

[![PyPI version](https://badge.fury.io/py/redlite.svg)](https://badge.fury.io/py/redlite)
[![Documentation](https://img.shields.io/badge/documentation-latest-brightgreen)](https://innodatalabs.github.io/redlite/)
[![Test and Lint](https://github.com/innodatalabs/redlite/actions/workflows/test.yaml/badge.svg)](https://github.com/innodatalabs/redlite)
[![GitHub Pages](https://github.com/innodatalabs/redlite/actions/workflows/docs.yaml/badge.svg)](https://github.com/innodatalabs/redlite)

An opinionated toolset for testing Conversational Language Models.

## Documentation

<https://innodatalabs.github.io/redlite/>

## Usage

1. Install required dependencies

    ```bash
    pip install redlite[all]
    ```

2. Generate several runs (using Python scripting, see [examples](https://github.com/innodatalabs/redlite/tree/master/samples), and below)

3. Review and compare runs

    ```bash
    redlite server --port <PORT>
    ```

4. Optionally, upload to Zeno

    ```bash
    ZENO_API_KEY=zen_XXXX redlite upload
    ```

## Python API

```python
import os
from redlite import run, load_dataset
from redlite.model.openai_model import OpenAIModel
from redlite.metric import MatchMetric


model = OpenAIModel(api_key=os.environ["OPENAI_API_KEY"])
dataset = load_dataset("hf:innodatalabs/rt-gaia")
metric = MatchMetric(ignore_case=True, ignore_punct=True, strategy='prefix')

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
* docs-server
* black

## Zeno <zenoml.com> integration

Benchmarks can be uploaded to Zeno interactive AI evaluation platform <hub.zenoml.com>:

```bash
redlite upload --project my-cool-project
```

All tasks will be concatenated and uploaded as a single dataset, with extra fields:

* `task_id`
* `dataset`
* `metric`

All models will be uploaded. If model was not tested on a specific task, a simulated zero-score dataframe is used instead.

Use `task_id` (or `dataset` as appropriate) to create task slices. Slices can be used to
navigate data or create charts.

## TODO

- [x] deps cleanup (randomname!)
- [x] review/improve module structure
- [x] automate CI/CD
- [x] write docs
- [x] publish docs automatically (CI/CD)
- [x] web UI styling
- [ ] better test server
- [ ] tests
- [x] Integrate HF models
- [x] Integrate OpenAI models
- [ ] Integrate Anthropic models
- [ ] Integrate vLLM models
- [x] Fix data format in HF datasets (innodatalabs/rt-* ones) to match standard
- [ ] more robust backend API (future-proof)
- [ ] better error handling for missing deps
- [ ] document which deps we need when
- [ ] export to CSV
- [x] Upload to Zeno
