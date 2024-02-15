from typing import Literal
from .. import NamedMetric
from .util import normalize_string


class MatchMetric(NamedMetric):
    """
    Metric that checks that the actual response matches expected string.

    For example, the expected response could be "Correct", but model answers
    "Correct, because blah blah blah...". To give model full marks for longer and
    verbose answer, use this metric.

    - **ignore_case** (`bool`, optional) - when set to `True` will ignore text case. Deafult is `False`.

    - **ignore_punct** (`bool`, optional) - when set to `True` punctuation symbols will be ignored.
            Default is `False`.

    - **normalize_white_space** (`bool`, optional) - when set to `True`, normalizes white space by
            replacing tabs and newlines with spaces and replacing multiple spaces to one. Also
            strips leading and trailing whitespace.
            Default is `False`.
    - **match** (`Literal["exact", "prefix", "contains"]`, optional) - determines how strings are matched.

        * `"exact"`: matches if expected and actual responses are the same
        * `"prefix"`: matches if actual response starts with the expected string
        * `"contains"`: matches if expected string is found anywhere in the actual response

        Default is `"exact"`.
    """

    def __init__(
        self,
        ignore_case=False,
        ignore_punct=False,
        normalize_whitespace=False,
        match: Literal["exact", "contains", "prefix"] = "prefix"):
        if match not in ("prefix", "contains", "exact"):
            raise ValueError(f"Invalid value of match parameter. Expect one of ('exact', 'prefix', 'contains'), got '{match}'")
        name = f"match-{match}"
        if ignore_case:
            name = name + "-ignore-case"
        if ignore_punct:
            name = name + "-ignore-punct"
        if normalize_whitespace:
            name = name + "-strip"

        self.ignore_case = ignore_case
        self.ignore_punct = ignore_punct
        self.normalize_whitespace = normalize_whitespace
        self.match = match

        super().__init__(name, self.__engine)

    def __engine(self, expected: str, actual: str) -> float:
        expected = normalize_string(
            expected,
            to_lower=self.ignore_case,
            strip_punct=self.ignore_punct,
            normalize_whitespace=self.normalize_whitespace,
        )
        actual = normalize_string(
            actual,
            to_lower=self.ignore_case,
            strip_punct=self.ignore_punct,
            normalize_whitespace=self.normalize_whitespace,
        )
        if self.match == "contains":
            return 1.0 if expected in actual else 0.0
        elif self.match == "prefix":
            return 1.0 if actual.startswith(expected) else 0.0
        elif self.match == "exact":
            return 1.0 if actual == expected else 0.0
        else:
            assert False  # not reached
