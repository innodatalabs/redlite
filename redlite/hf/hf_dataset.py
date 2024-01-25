from collections.abc import Iterator
from ..core import NamedDataset, DatasetItem, user_message, MissingDependencyError


try:
    from datasets import load_dataset
    from huggingface_hub import DatasetCard
except ImportError as err:
    raise MissingDependencyError("Please install datasets library") from err


class HFDataset(NamedDataset):
    def __init__(self, hf_name: str, split="test"):
        super().__init__()
        self.name = "hf:" + hf_name + "@" + split
        self._dataset = load_dataset(hf_name, trust_remote_code=True)
        self._card = DatasetCard.load(hf_name)
        self.labels = getattr(self._card.data, "labels", {})
        self._split = split

    def __iter__(self) -> Iterator[DatasetItem]:
        for x in self._dataset[self._split]:
            prompt = x["prompt"]
            completion = x["completion"]
            id_ = x["id"]

            yield dict(
                id=id_,
                messages=[user_message(prompt)],
                expected=completion,
            )

    def __len__(self):
        return self._dataset[self._split].info.splits[self._split].num_examples

    @classmethod
    def load(cls, name: str, split="test") -> "NamedDataset":
        if not name.startswith("hf:"):
            raise ValueError(f"This method can only load from HF dataset hub, but requested {name}")
        return cls(name[3:], split)
