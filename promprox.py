#!/usr/bin/python3
"""This python scripts reads an external Prometheus metrics page and
makes it available within the Kubernetes cluster itself. This is perfect
for a setup where you don't want to hardcode your Prometheus targets"""
import os
import json
import requests
from flask import Flask

APP = Flask(__name__)

if "METRIC_URL" in os.environ:
    PROM_METRIC_URL = str(os.environ["METRIC_URL"])
else:
    print("Please set the METRIC_URL environmental variable")

if "PROM_HEADER" in os.environ:
    PROM_HEADER = str(os.environ["PROM_HEADER"])

@APP.route("/")
def home():
    """This function returns the main page output."""
    return f"""This it the Prometheus Metric Proxy. Currently in use for url {PROM_METRIC_URL}.
    Go to the /metrics path to retrieve the external metrics."""


@APP.route("/metrics")
def get_metrics():
    """This function requests the external url and returns the output."""
    source = requests.Session()

    if 'PROM_HEADER' in globals():
        header = json.loads(PROM_HEADER)
        source.headers.update(header)

    response = source.get(PROM_METRIC_URL)

    if response.status_code == 200:
        return response.content.decode("utf-8")
    return response.status_code


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=9090)
