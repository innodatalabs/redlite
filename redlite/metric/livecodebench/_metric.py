import json
import re
from urllib.request import urlopen, Request
from redlite import NamedMetric


class LiveCodeBenchMetric(NamedMetric):
    """
    Metric to score Python code generation agains input/output tests.

    This metric is specific to the LiveCodeBench benchmark and interacts with a local server that runs
    the generated code against the test cases.

    Server is a docker built from a GitHub
    [redlite-livecodebench-grader](https://github.com/innodatalabs/redtite-livecodebench-grader/) repository.

    After building server docker, run it like this:

    ```bash
    docker run -it -p 8000:80 ilabs/redlite-livecodebench-grader:latest
    ```

    - **endpoint** (`str`, optional): URL of server running the grading service. Default is `http://localhost:8000`.
    """

    def __init__(self, endpoint: str = "http://localhost:8000"):
        self.endpoint = endpoint
        super().__init__("livecodebench-metric", self._score)

    def _score(self, expected: str, actual: str) -> float:
        pieces = re.split(r"`python\n(.*?)```", actual, flags=re.DOTALL)
        if len(pieces) < 2:
            return 0.0
        code = pieces[-2]

        datum = json.loads(expected)
        fn_name = datum.get("name")
        testtypes = set(x["testtype"] for x in datum["tests"])
        if len(testtypes) != 1:
            raise RuntimeError("Mixed test types not supported")
        testtype = testtypes.pop()
        inputs = [x["input"] for x in datum["tests"]]
        outputs = [x["output"].strip() for x in datum["tests"]]
        assert len(inputs) == len(outputs) and len(inputs) > 0, "Broken test"

        request = Request(
            f"{self.endpoint}/run_test/{testtype}",
            method="POST",
            headers={
                "Content-type": "application/json",
            },
            data=json.dumps(
                {
                    "code": code,
                    "inputs": inputs,
                    "outputs": outputs,
                    "name": fn_name,
                    "timeout": 5,
                }
            ).encode("utf-8"),
        )
        with urlopen(request) as response:
            if response.getcode() != 200:
                raise RuntimeError(f"Error from server: {response.status_code} {response.text}")
            out = json.loads(response.read().decode("utf-8"))
            if out["success"] is not True:
                return 0.0
        return 1.0
