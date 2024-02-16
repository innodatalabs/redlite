from typing import Iterator
from redlite import NamedDataset, DatasetItem
from redlite._util import format_duration, parse_duration, DatasetRunningDigest


def test_parse_duration():
    assert parse_duration("1.5s") == 1.5
    assert parse_duration("2m 33.5s") == 120 + 33.5
    assert parse_duration("1h") == 60 * 60
    assert parse_duration("1d") == 60 * 60 * 24


def test_format_duration():
    assert format_duration(60 * 60 * 24) == "1d 0h 0m 0s"


def test_format_duration_float():
    assert format_duration(60 * 60 * 24.0) == "1d 0h 0m 0.0s"


def test_parse_duration_float():
    assert parse_duration("1d 0h 0m 0.0s") == 60 * 60 * 24.0


class MockDataset(NamedDataset):
    def __init__(self, *, name, split="test", labels={}, data):
        self.labels = labels
        self.data = data
        self.name = name
        self.split = split

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> Iterator[DatasetItem]:
        yield from self.data


ITEM1 = {
    "id": "1",
    "messages": [
        {"role": "user", "content": "Hello, world!"},
    ],
    "expected": "ACCEPT",
}

ITEM2 = {
    "id": "2",
    "messages": [
        {"role": "user", "content": "Good bye, cruel, world!"},
    ],
    "expected": "REJECT",
}

ITEM3 = {
    "id": "3",
    "messages": [
        {"role": "user", "content": "Is you work boring? Join Innodata!"},
    ],
    "expected": "MELT",
}


def test_order_independent_dataset_hashing():
    dataset = DatasetRunningDigest(MockDataset(name='mock', data=[ITEM1, ITEM2]))
    for x in dataset:
        pass
    digest1 = dataset.hexdigest

    dataset = DatasetRunningDigest(MockDataset(name='mock', data=[ITEM2, ITEM1]))
    for x in dataset:
        pass
    digest2 = dataset.hexdigest

    assert digest1 == digest2

    dataset = DatasetRunningDigest(MockDataset(name='mock', data=[ITEM1, ITEM3]))
    for x in dataset:
        pass
    digest3 = dataset.hexdigest

    assert digest3 != digest1
