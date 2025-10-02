FROM python:3.11

WORKDIR /app

COPY app.py .
COPY templates ./templates

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY scripts .

RUN chmod +x download-translations.sh
RUN ./download-translations.sh

CMD ["/bin/bash", "./entrypoint.sh"]