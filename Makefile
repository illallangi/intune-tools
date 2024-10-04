.PHONY: help
help:
	@echo "make pip"
	@echo "       Install all dependencies using pip"
	@echo "make black"
	@echo "       Run black to format the code"
	@echo "make flake8"
	@echo "       Run flake8 to lint the code"
	@echo "make clean"
	@echo "       Remove all temporary files"
	@echo "make cache"
	@echo "       Generate cache files"
	@echo "make policies.xlsx"
	@echo "       Generate policies.xlsx file"

.PHONY: pip
pip:
	pip install -r requirements.txt

.PHONY: black
black:
	python3 -m black --quiet .

.PHONY: flake8
flake8:
	python3 -m flake8 .

.PHONY: clean
clean:
	rm -rf __pycache__ .pytest_cache
	rm -f *.json policies.xlsx
	
.PHONY: cache
cache: lint format
	python3 -m intune_documenter category > /dev/null
	python3 -m intune_documenter policy > /dev/null
	python3 -m intune_documenter policy-assignment > /dev/null
	python3 -m intune_documenter policy-setting > /dev/null
	python3 -m intune_documenter setting > /dev/null

.PHONY: policies.xlsx
policies.xlsx: lint format
	python3 -m intune_documenter xlsx c9b8ba65-ffb3-4dd3-8076-0d3d835686d3 ce6b7602-3b21-4ed0-bfae-2b2b728a09fc
