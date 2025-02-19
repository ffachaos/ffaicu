# Makefile

.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help message
ifeq ($(OS),Windows_NT)
	@chcp 65001 > nul
	@for /f "tokens=1,* delims=:" %%A in ('findstr /R "^[a-zA-Z_-]*:.*##" $(MAKEFILE_LIST)') do ( \
	    for /f "tokens=1,* delims=##" %%i in ("%%B") do @echo %%A    %%j \
	)
else
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'
endif

.PHONY: shebang
shebang: ## shebangを任意のパスに変更する (e.g. make shebang SHEBANG="/usr/local/bin/perl --")
ifeq ($(OS),Windows_NT)
	@echo TODO
else
	@bash scripts/sh/shebang.sh $(SHEBANG)
endif

.PHONY: up
up: ## Dockerコンテナを起動する
	@docker-compose up -d --build
ifeq ($(OS),Windows_NT)
	@chcp 65001 > nul
	@echo 🚀 Server has started successfully!
	@echo 📌 Open your browser and visit:
	@echo    🔗 http://localhost:8008
	@echo 💡 make down to stop the server.
else
	@echo "\033[36m🚀 Server has started successfully!\033[0m"
	@echo "\033[36m📌 Open your browser and visit:\033[0m"
	@echo "\033[36m   🔗 http://localhost:8008\033[0m"
	@echo "\033[36m💡 make down to stop the server.\033[0m"
endif


.PHONY: down
down: ## Dockerコンテナを停止する
	@docker-compose down

.PHONY: build
build: ## Dockerコンテナをbuildする
	@docker-compose build

