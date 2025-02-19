# Makefile

.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

.PHONY: shebang
shebang: ## shebangを任意のパスに変更する (e.g. make shebang SHEBANG="/usr/local/bin/perl --")
	@bash scripts/shebang.sh $(SHEBANG)

.PHONY: up
up: ## Dockerコンテナを起動する
	@docker-compose up -d --build

.PHONY: down
down: ## Dockerコンテナを停止する
	@docker-compose down

.PHONY: build
build: ## Dockerコンテナをbuildする
	@docker-compose build