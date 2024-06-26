# Define the default target
all: setup run expose-ngrok

# Define the setup target
setup:
		@echo "Running application setup script..."
		./scripts/app_setup.sh

run:
		@echo "Running application..."
		./scripts/app_run.sh

expose-ngrok:
		@echo "Exposing application to the internet..."
		./scripts/expose_ngrok.sh

.PHONY: all setup run