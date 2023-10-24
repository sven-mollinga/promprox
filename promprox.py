#!/usr/bin/python3
"""This python scripts reads an external prometheus metrics page and
makes it available within the kubernetes cluster itself. This is perfect
for a setup where you don't want to hardcode your prometheus targets"""
import os
import requests
from flask import Flask

APP = Flask(__name__)
PROM_METRIC_URL = str(os.environ["METRIC_URL"])


@APP.route("/")
def home():
    """This function returns the main page output."""
    return f"""This it the Prometheus Metric Proxy. Currently in use for url {PROM_METRIC_URL}.
    Go to the /metrics path to retrieve the external metrics."""


@APP.route("/metrics")
def get_metrics():
    """This function requests the external url and returns the output."""
    response = requests.get(PROM_METRIC_URL)
    if response.status_code == 200:
        return response.content.decode("utf-8")
    return "Not Found"


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=9090)
