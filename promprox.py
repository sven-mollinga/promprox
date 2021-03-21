#!/usr/bin/python3
import requests
from flask import Flask
from flask import request
app = Flask(__name__)
import os

prom_metric_url = str(os.environ['METRIC_URL'])

@app.route('/')
def home():
    return 'This it the Prometheus Metric Proxy. Currently in use for url {}. Go to the /metrics path to retrieve the external metrics.'.format(prom_metric_url)

@app.route('/metrics')
def get_metrics():
    response = requests.get(prom_metric_url)
    if response.status_code == 200:
        return(response.content.decode("utf-8"))
    elif response.status_code == 404:
        return('Not Found.')

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=9090)