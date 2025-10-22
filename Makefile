run-debug:
	flask run --debug --port 8000

# Requests

search-phrase-whitespace:
	http://127.0.0.1:8000/search?translation=BSB&phrase=I+desire+mercy&book=matt&chapter=&testament=

# Docker

build:
	docker compose build

bash:
	docker run -it berea-wsgi /bin/bash

up:
	docker compose up

down:
	docker compose down