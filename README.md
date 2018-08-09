Proof-of-concept project to run many flask-uwsgi-nginx docker containers on the same host port (`8080`) with different url paths using nginx reverse proxy.

# Usage

`docker-compose build`

then

`docker-compose up`

or

`docker-compose up -d` to run in background

# Output

Dockerized flask APP 1 (contained in `docker-app-1`) is served on:
- [http://127.0.0.1:5000](http://127.0.0.1:5000)
- [http://127.0.0.1:8080/app1/](http://127.0.0.1:8080/app1/)

Dockerized flask APP 2 (contained in `docker-app-2`) is served on:
- [http://127.0.0.1:5001](http://127.0.0.1:5001)
- [http://127.0.0.1:8080/app2/](http://127.0.0.1:8080/app2/)
