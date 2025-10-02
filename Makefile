run:
	flask run --debug --port 8000

# Requests

search-phrase-whitespace:
	http://127.0.0.1:8000/search?translation=BSB&phrase=I+desire+mercy&book=matt&chapter=&testament=