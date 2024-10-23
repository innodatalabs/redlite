from redlite import run
from redlite.dataset.memory_dataset import MemoryDataset
from redlite.model.llamacpp_model import LllamaCppModel
from redlite.metric import RandomMetric

model = LllamaCppModel("./models/mistral-7b-instruct-v0.2.Q2_K.gguf", n_ctx=512, max_tokens=512)

dataset = MemoryDataset(data=[
    {
        'id': '1',
        'messages': [ {'role': 'user', 'content': 'Who was the president of the US in 2015? Be short!'}],
        'expected': ''
    }
], name='test-memory-dataset')

run(model=model, dataset=dataset, metric=RandomMetric())

