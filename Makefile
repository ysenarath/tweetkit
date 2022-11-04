VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/python3 -m pip
DIST = dist

upload: $(DIST)
	twine upload $(DIST)/*

test-upload: $(DIST)
	twine upload -r testpypi $(DIST)/*

$(DIST): build

build: $(VENV)/bin/activate
	rm -rf dist
	rm -rf tweetkit.egg-info
	$(VENV)/bin/python3 -m build

setup: requirements.txt $(VENV)/bin/activate
	$(PIP) install -r requirements.txt

requirements.txt: $(VENV)/bin/activate
	$(PIP) install pip-tools
	pip-compile -o requirements.txt --extra dev

$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip

clean:
	rm -rf tweetkit.egg-info
	rm -rf dist
	rm -rf __pycache__
	rm -rf venv