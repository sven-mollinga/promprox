# promprox
A Prometheus metrics proxy to use in a Kubernetes environment to reach external applications without hardcording scrape config

## Run on docker
You can run the proxy on docker with the following command. In this case we use the URL external-proxy-url.example.com:8000 as our remote prometheus metric endpoint.
```
sudo docker run -d -p 9090:9090 --name promprox -e METRIC_URL=external-proxy-url.example.com:8000 svenmollinga/promprox:latest
```