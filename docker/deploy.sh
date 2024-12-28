#!/bin/bash
# Run this from the repo root.

set -euo pipefail

# $1 - version

tag="539715613711.dkr.ecr.us-east-1.amazonaws.com/quasilabs/lpbook:$1"

# Build and tag image
docker build --pull -t $tag -f docker/Dockerfile .

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 539715613711.dkr.ecr.us-east-1.amazonaws.com && \
docker push $tag
