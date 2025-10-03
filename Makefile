run-debug:
	flask run --debug --port 8000

# Requests

search-phrase-whitespace:
	http://127.0.0.1:8000/search?translation=BSB&phrase=I+desire+mercy&book=matt&chapter=&testament=

build:
	docker build -t berea:latest .

bash:
	docker run -it berea /bin/bash

up:
	docker compose up

down:
	docker compose down