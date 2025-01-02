



### Crear alias
- alias reset_docker='echo "Source .env" && source .env && echo "Down Docker" && make down && clear && echo "Down Build Docker" && make build && clear && echo "Up Detach" && make up-d'

#### Ejecutar con el alias y el make
- reset_docker && make up


### Migraciones con alembic

- alembic revision --autogenerate -m "migration"
- alembic upgrade heads

