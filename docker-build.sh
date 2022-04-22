#!/bin/bash
TAG=$(date '+%Y%m%d')
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
NAME=$(basename "$SCRIPT_DIR")
docker build -t rzarajczyk/$NAME:$TAG .
docker tag rzarajczyk/$NAME:$TAG rzarajczyk/$NAME:latest
docker push rzarajczyk/$NAME:$TAG
docker push rzarajczyk/$NAME:latest
