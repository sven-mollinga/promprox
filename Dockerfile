# Prometheus Metrics Proxy
#
# https://github.com/sven-mollinga/promprox/blob/main/Dockerfile
#

# Use Python base image
FROM python:3.10.2-alpine3.15

COPY . .

RUN pip3 install -r requirements.txt

CMD python3 promprox.py
