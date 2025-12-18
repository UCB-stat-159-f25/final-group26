SHELL := /bin/bash

ENV_NAME := traffic-fatalities
ENV_FILE := environment.yml

NOTEBOOKS := $(shell find notebooks -name "*.ipynb" \
	-not -path "*/.ipynb_checkpoints/*")

env:
	@if conda env list | grep -q "^$(ENV_NAME)[[:space:]]"; then \
		conda env update -n $(ENV_NAME) -f $(ENV_FILE) --prune; \
	else \
		conda env create -f $(ENV_FILE); \
	fi

all:
	@for nb in $(NOTEBOOKS); do \
		echo "Running $$nb"; \
		conda run -n $(ENV_NAME) jupyter nbconvert --execute --to notebook --inplace "$$nb"; \
	done