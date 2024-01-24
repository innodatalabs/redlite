import dataclasses
import abc
from collections.abc import Callable, Iterable
from typing import Any, TypedDict, Literal
import logging


log = logging.getLogger("redlite")


Role = Literal["system", "user", "assistant"]
"""Type for the message role"""

Message = TypedDict("Message", {"role": Role, "content": str})
"""Message has content and role"""

Messages = list[Message]
"""Messages is just a list of ... messages!"""

Batch = list[Messages]
"""Messages can be batched for faster evaluation (i.e. on a GPU)"""

DatasetItem = TypedDict("DatasetItem", {"id": str, "messages": Messages, "expected": str})
"""Unique id, sessages, and the expected completion"""


def system_message(content: str) -> Message:
    return {"role": "system", "content": content}


def user_message(content: str) -> Message:
    return {"role": "user", "content": content}


def assistant_message(content: str) -> Message:
    return {"role": "assistant", "content": content}


class NamedDataset(Iterable[DatasetItem]):
    name: str


class NamedMetric:
    name: str

    def __init__(self, name: str, engine: Callable[[str, str], float]):
        self.name = name
        self.engine = engine

    def __call__(self, expected: str, actual: str) -> float:
        return self.engine(expected, actual)


class NamedModel:
    name: str

    def __init__(self, name: str, engine: Callable[[Messages], str]):
        self.name = name
        self.engine = engine

    def __call__(self, conversation: Messages) -> str:
        return self.engine(conversation)


class Storage(abc.ABC):
    def __init__(self, name: str):
        self.name = name

    @abc.abstractmethod
    def save(self, item: DatasetItem, response: str, score: float):
        pass

    @abc.abstractmethod
    def save_meta(self, **kw):
        pass


@dataclasses.dataclass
class Experiment:
    """Represents experiment run"""

    name: str


class MissingDependencyError(RuntimeError):
    """Raised when a missing optional dependency is detected"""


KeyedValues = dict[str, Any]

ScoreSummary = TypedDict("ScoreSummary", {"count": int, "mean": float, "min": float, "max": float})


class ScoreAccumulator:
    def __init__(self):
        self._min = 100000  # FIXME?
        self._max = 0.0
        self._acc = 0.0
        self._count = 0

    def __call__(self, score: float) -> None:
        self._acc += score
        self._min = min(self._min, score)
        self._max = max(self._max, score)
        self._count += 1

    @property
    def summary(self) -> ScoreSummary:
        mean = 0.0 if self._count == 0 else self._acc / self._count
        return dict(
            count=self._count,
            mean=mean,
            min=self._min,
            max=self._max,
        )
