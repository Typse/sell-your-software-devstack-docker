# Dev Stack (WordPress + remote MariaDB + FastAPI + Nginx)

## Quickstart
```bash

.env datei einfügen

docker compose up -d --build

# WordPress: http://localhost/
# Adminer:  http://localhost/db/  (Server: steht in der env)
# API:      http://localhost/api/health
# Mailhog:  http://localhost/mail/

Falls der Installer erscheint hilft
docker run --rm mariadb:11 mariadb -h 5.9.67.189 -P 13306 -u sellyoursystem -p sellyoursystem123 -e "SELECT 1" sys-wp

# Nützliche Commands
docker compose ps
docker compose logs -f wordpress
docker compose run --rm --user 33:33 wpcli wp user list
