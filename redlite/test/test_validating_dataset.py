from redlite.dataset import ValidatingDataset
import pytest


class SampleDataset:
    def __init__(self, *, split="test", name="a sample dataset", labels={}, samples):
        self.name = name
        self.split = split
        self.labels = labels
        self._samples = samples

    def __len__(self):
        return len(self._samples)

    def __iter__(self):
        yield from self._samples


def test_smoke():
    samples = [
        {
            "id": "123",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": "Lets play a game"},
            ],
            "expected": "As a helpful assistant I can not play games",
        }
    ]
    dataset = ValidatingDataset(SampleDataset(samples=samples))

    assert len(dataset) == 1
    assert dataset.name == "a sample dataset"
    assert dataset.split == "test"

    assert list(dataset) == samples
    assert list(dataset) == samples  # can iterate again


def test_validate_item():
    dataset = ValidatingDataset(SampleDataset(samples=[1, 2, 3]))

    with pytest.raises(RuntimeError, match="Invalid dataset.*: item is not a dict! Here is what I've seen: 1"):
        list(dataset)


def test_validate_item_keys():
    dataset = ValidatingDataset(SampleDataset(samples=[{}]))

    with pytest.raises(
        RuntimeError, match='Invalid dataset .*: item does not have required "id" key, or value is not str'
    ):
        list(dataset)


def test_validate_item_keys_01():
    dataset = ValidatingDataset(SampleDataset(samples=[{"id": "1", "messages": 2, "expected": "something"}]))

    with pytest.raises(
        RuntimeError,
        match='Invalid dataset .*: item with id 1 does not have required "messages" key, or its value is not a list',
    ):
        list(dataset)


def test_validate_item_keys_02():
    dataset = ValidatingDataset(
        SampleDataset(
            samples=[
                {
                    "id": "1",
                    "messages": [],
                    "expected": "something",
                }
            ]
        )
    )

    with pytest.raises(RuntimeError, match="Invalid dataset .*: item with id 1 has zero-length messages array"):
        list(dataset)


def test_validate_item_keys_03():
    dataset = ValidatingDataset(
        SampleDataset(
            samples=[
                {
                    "id": "1",
                    "messages": [{}],
                    "expected": "something",
                }
            ]
        )
    )

    with pytest.raises(
        RuntimeError,
        match="Invalid dataset .*: item with id 1 has malformed messages array "
        + '\\(expect dict values with "role" and "content" keys\\)',
    ):
        list(dataset)


def test_validate_item_keys_04():
    dataset = ValidatingDataset(
        SampleDataset(
            samples=[
                {
                    "id": "1",
                    "messages": [{"role": "system", "content": "hoho"}],
                    "expected": "something",
                }
            ]
        )
    )

    with pytest.raises(
        RuntimeError,
        match="Invalid dataset .*: item with id 1 has malformed messages array "
        + '\\(expect last message to be from "user"\\)',
    ):
        list(dataset)


def test_validate_duplicate_ids():
    dataset = ValidatingDataset(
        SampleDataset(
            samples=[
                {
                    "id": "1",
                    "messages": [{"role": "user", "content": "hoho"}],
                    "expected": "something",
                },
                {
                    "id": "1",
                    "messages": [{"role": "user", "content": "hoho"}],
                    "expected": "something",
                },
            ]
        )
    )

    with pytest.raises(RuntimeError, match="Invalid dataset .*: duplicate item id: {'id': '1'"):
        list(dataset)
