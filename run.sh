#!/bin/bash
app="flask-api"
docker build -t ${app} .
docker run -d -p 8080:8080 \
   ${app}
