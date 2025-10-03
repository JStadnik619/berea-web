run-debug:
	flask run --debug --port 8000

# Requests

search-phrase-whitespace:
	http://127.0.0.1:8000/search?translation=BSB&phrase=I+desire+mercy&book=matt&chapter=&testament=

build:
	docker build -t berea:latest .

it:
	docker run -it berea /bin/bash

# BUG: Site can't be reached
# Run a container that's killable via ctrl+c in same shell
run:
	docker run --name berea --init -it berea