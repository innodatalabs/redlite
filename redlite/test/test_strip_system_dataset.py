from collections.abc import Iterator
from redlite.dataset import StripSystemDataset
from redlite import NamedDataset, DatasetItem


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


def test_smoke():
    dataset = MockDataset(
        name="foo",
        data=[
            {
                "id": "1",
                "messages": [
                    {"role": "system", "content": "I am helpful"},
                    {"role": "user", "content": "Hello"},
                ],
                "expected": "boo",
            },
        ],
    )

    wrapped = StripSystemDataset(dataset)
    assert wrapped.name == "foo-strip-system"
    assert len(wrapped) == 1

    data = list(wrapped)

    assert len(data) == 1
    assert data[0] == {
        "id": "1",
        "messages": [
            {"role": "user", "content": "Hello"},
        ],
        "expected": "boo",
    }
