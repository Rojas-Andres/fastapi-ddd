# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

.PHONY: help

.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

black: ## black
	black . --line-length=79 --exclude migrations\

docker-login: ## docker login
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com

build: ## build
	docker compose build

up: ## up
	docker compose up

up-d: ## up d
	docker compose up -d

down: ## down
	docker compose down --remove-orphans

down-d: ## down
	docker compose down --remove-orphans --rmi local

run:  ## run
	docker compose run --rm --service-ports worker ${args}

celery: ## run celery
	docker compose run --rm --entrypoint=celery worker -A app.infrastructure.messaging.app worker -l info

exec-celery: ## exec celery
	docker compose exec worker celery -A app.infrastructure.messaging.app worker -l info

beat: ## run celery beat
	docker compose run --rm --entrypoint=celery worker -A app.infrastructure.messaging.app beat

docker-celery: ## docker celery
	docker exec -it ${CONTAINER_ID} celery -A app.infrastructure.messaging.app worker -l info

docker-attach: ## docker attach
	docker attach --detach-keys ctrl-d ${CONTAINER_ID}

dev-check: ##Run all pre-commit hooks.
	@pre-commit run --all-files
