default:
	@cat makefile

env:
	python3 -m venv env
	pip install -r requirements.txt
    
run:
	@./env/bin/python3 /home/ubuntu/DS5111_FALL2023_SW2_Lab/bin/clockdeco_param.py
    

.PHONY: tests
tests:
	pytest -vv tests
