#!/usr/bin/env bash
docker build -t python-benchmark .
docker run -v $(pwd)/output:/app/output -e MAX=10000000000 -e SCALE=1000000000 -e MODES="isolated" --cpus=1 python-benchmark