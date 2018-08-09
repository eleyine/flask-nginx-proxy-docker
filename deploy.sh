#! /usr/bin/env bash
docker-compose down
docker-compose build --force-rm --no-cache
# docker-compose up -d
docker-compose up
