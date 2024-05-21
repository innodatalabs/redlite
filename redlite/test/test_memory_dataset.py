from redlite.dataset.memory_dataset import MemoryDataset


def test_memory_dataset():

    dataset = MemoryDataset(name="my-dataset", data=[])

    assert dataset.split == "test"
    assert dataset.name == "my-dataset"
    assert len(dataset) == 0
