
all: run

install:
	sudo python3.7 -m pip install -r requirements.txt

run:
	python3.7 manage.py run
