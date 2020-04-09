#!/bin/sh
test ! -z "$(docker ps -aqf name=c-flaskd-stg)" && docker rm -f c-flaskd-stg && echo "container staging removed"
test ! -z "$(docker images -q i-flaskd-stg)" && docker rmi i-flaskd-stg && echo "image staging removed"

docker build -t i-flaskd-stg .
docker run -d -p 5000:4000 --name c-flaskd-stg i-flaskd-stg