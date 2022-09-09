run:
	python3 app/main.py

install:
	pip3 install -r requirements.txt

test:
	pytest -qv tests/test_*.py

greeting:
	python3 hello_world.py