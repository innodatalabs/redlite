from redlite.model import ParrotModel, CannedModel


def test_parrot():
    parrot = ParrotModel()

    answer = parrot([{"role": "user", "content": "Hello"}])
    assert answer == "Hello"


def test_canned():
    canned = CannedModel("Bye")

    answer = canned([{"role": "user", "content": "Hello"}])
    assert answer == "Bye"
