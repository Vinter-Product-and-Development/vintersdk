test:
	pytest -v --cov=vintersdk --disable-pytest-warnings &&\
		readme-cov

testhtml:
	pytest -v --cov=vintersdk --cov-report=html --disable-pytest-warnings &&\
		readme-cov

install:
	pip install --upgrade pip &&\
		python -m pip install -r requirements.txt

doc:
	cd docs && make html

mkdocs-serve:
	mkdocs serve

readme-cp:
	cp README.md mdocs/index.md &&\
		cp examples.md mdocs/examples.md &&\
		cp multi_asset.md mdocs/multi_asset.md &&\
		cp single_asset.md mdocs/single_asset.md &&\
		cp websocket.md mdocs/websocket.md

mkdocs-build:
	mkdocs build

mkdocs: readme-cp mkdocs-build

pre-commit-file:
	pre-commit install

format:
	python3 -m black -l 79 --target-version py38 --exclude venv .

lint:
	python3 -m flake8 \
		--ignore=E203,E266,E501,W503 \
		--max-line-length=110 \
		--verbose \
		--exclude=./docs/*,mdocs \

requirements:
	pip freeze > requirements.txt

all: format test testhtml mkdocs lint requirements