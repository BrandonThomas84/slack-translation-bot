# Define the default target
all: setup run

# Define the setup target
setup:
		@echo "Running application setup script..."
		./scripts/app_setup.sh

run:
		@echo "Running application..."
		./scripts/app_run.sh

.PHONY: all setup run