from .core import NamedDataset, DatasetItem
from typing import Literal, Callable
from collections.abc import Iterator

__docformat__ = "google"


def load_dataset(name: str, split: Literal["test", "train"] = "test") -> NamedDataset:
    """Loads dataset. Downloads it to the local machine if necessary.

    Args:
        name (str): Dataset name. Starts with hub prefix "hf:" (HuggingFace datasets hub),
            or "inno:" (Innodata datasets hub)
        split (str): Split name ("test" or "train")

    Returns:
        NamedDataset: Dataset object.
    """
    dataset_loader = _get_dataset_loader(name)
    dataset = dataset_loader(name, split)
    return ValidatingDataset(dataset)


class ValidatingDataset(NamedDataset):
    """Wraps dataset and validates it."""

    def __init__(self, dataset: NamedDataset):
        """Creates instance from a dataset.

        Args:
            dataset (NamedDataset): A dataset to validate.
        """
        self._dataset = dataset
        self.name = dataset.name
        self.split = dataset.split
        self.labels = dict(dataset.labels)
        self._length = len(self._dataset)
        self._seen_ids: set[str] = set()

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Iterator[DatasetItem]:
        self._seen_ids.clear()
        for item in self._dataset:
            if not isinstance(item, dict):
                raise RuntimeError(
                    f"Invalid dataset {self._dataset}: item is not a dict! Here is what I've seen: {item}"
                )
            if "id" not in item or type(item["id"]) is not str:
                raise RuntimeError(
                    f'Invalid dataset {self._dataset}: item does not have required "id" key, or value is not str'
                )
            if "messages" not in item or type(item["messages"]) is not list:
                raise RuntimeError(
                    f"Invalid dataset {self._dataset}: item with id {item['id']} does not have "
                    + f'required "messages" key, or its value is not a list. Here is what I\'ve seen: {item}'
                )
            if len(item["messages"]) == 0:
                raise RuntimeError(
                    f"Invalid dataset {self._dataset}: item with id {item['id']} has "
                    + f"zero-length messages array. Here is what I've seen: {item}"
                )
            if not all(type(message) is dict and message.keys() == {"role", "content"} for message in item["messages"]):
                raise RuntimeError(
                    f"Invalid dataset {self._dataset}: item with id {item['id']} has "
                    + 'malformed messages array (expect dict values with "role" and "content" keys). '
                    + f"Here is what I've seen: {item}"
                )
            if item["messages"][-1]["role"] != "user":
                raise RuntimeError(
                    f"Invalid dataset {self._dataset}: item with id {item['id']} has "
                    + 'malformed messages array (expect last message to be from "user"). '
                    + f"Here is what I've seen: {item}"
                )
            if item["id"] in self._seen_ids:
                raise RuntimeError(f"Invalid dataset {self._dataset}: duplicate item id: {item}")
            yield item
            self._seen_ids.add(item["id"])


def _get_dataset_loader(name: str) -> Callable[[str, Literal["test", "train"]], NamedDataset]:
    if name.startswith("hf:"):
        from .hf.hf_dataset import HFDataset

        return HFDataset.load

    elif name.startswith("inno:"):
        from inno.inno_dataset import load_dataset as ld

        return ld

    else:
        raise ValueError(f"Unknown dataset hub: {name}")
