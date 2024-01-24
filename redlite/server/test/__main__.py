from .conftest import get_test_app
from aiohttp import web


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", "8000"))

    web.run_app(get_test_app(), port=port)
