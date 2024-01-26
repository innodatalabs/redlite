.PHONY: test
test:
	python -m pytest redlite/test

.PHONY: test-server
test-server:
	python -m pytest redlite/server/test

.PHONY: lint
lint: test
	flake8 --max-line-length 120 redlite/
	black -l 120 --check redlite/
	mypy --ignore-missing-imports redlite/

.PHONY: black
black:
	black -l 120 redlite/

.PHONY: docs
docs:
	@echo "building documentation ..."
	portray as_html --overwrite
	URL="site/index.html"; xdg-open $$URL || sensible-browser $$URL || x-www-browser $$URL || gnome-open $$URL || open $$URL

.PHONE: wheel
wheel:
	pip wheel . --no-deps -w wheels/
