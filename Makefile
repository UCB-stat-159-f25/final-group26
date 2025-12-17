# ---------- config ----------
ENV_NAME ?= sotu
ENV_FILE ?= environment.yml
NB_DIR   ?= .
NBS      := $(shell ls $(NB_DIR)/*.ipynb 2>/dev/null)

# Conda shell hook (needed so "conda activate" works inside make)
CONDA_BASE := $(shell conda info --base 2>/dev/null)
CONDA_SH   := $(CONDA_BASE)/etc/profile.d/conda.sh

# Use the env's python so nbconvert runs with the right deps
PY_IN_ENV := bash -lc "source '$(CONDA_SH)' && conda activate '$(ENV_NAME)' && python"

.PHONY: env all export

# ---------- targets ----------
env: $(ENV_FILE)
	@bash -lc "source '$(CONDA_SH)' && \
	if conda env list | awk '{print $$1}' | grep -qx '$(ENV_NAME)'; then \
		echo '[env] Updating existing env: $(ENV_NAME)'; \
		conda env update -n '$(ENV_NAME)' -f '$(ENV_FILE)' --prune; \
	else \
		echo '[env] Creating env: $(ENV_NAME)'; \
		conda env create -n '$(ENV_NAME)' -f '$(ENV_FILE)'; \
	fi"

all: env
	@if [ -z "$(NBS)" ]; then echo "[all] No notebooks found in $(NB_DIR)"; exit 0; fi
	@for nb in $(NBS); do \
		echo "[all] Running $$nb"; \
		$(PY_IN_ENV) -m jupyter nbconvert --to notebook --execute "$$nb" --inplace; \
	done
	@echo "[all] Done."

# Optional: regenerate environment.yml from the current env (portable-ish)
export:
	@bash -lc "source '$(CONDA_SH)' && conda activate '$(ENV_NAME)' && \
	conda env export --no-builds | grep -v '^prefix:' > '$(ENV_FILE)' && \
	echo '[export] Wrote $(ENV_FILE)'"
