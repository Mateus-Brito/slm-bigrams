.PHONY: help install uninstall reinstall version run
.DEFAULT_GOAL := help
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

define PRINT_HELP_PYSCRIPT
import re, sys
for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?$$', line)
	if match:
		target = match.groups()
		print("%s" % (target))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

$(VENV)/bin/activate: requirements.txt
	@python3.10 -m venv $(VENV)
	@$(PIP) install -U pip
	@$(PIP) install -r requirements.txt

install: $(VENV)/bin/activate

uninstall:
	@rm -rf $(VENV)

reinstall: uninstall install

run: $(VENV)/bin/activate
	@$(VENV)/bin/python app.py

version: $(VENV)/bin/activate
	@$(PYTHON) --version
	@$(PIP) --version
	@$(PIP) freeze
