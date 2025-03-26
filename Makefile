
.PHONY: setup env clean test lint format train eval export api ui docs docker help

# Default target
help:
	@echo "Available commands:"
	@echo "  make setup       - Set up initial project structure"
	@echo "  make env         - Create Python virtual environment using uv"
	@echo "  make clean       - Clean temporary files and caches"
	@echo "  make test        - Run tests"
	@echo "  make lint        - Run linters (ruff)"
	@echo "  make format      - Format code (black, isort)"
	@echo "  make train       - Train model with default configuration"
	@echo "  make eval        - Evaluate model"
	@echo "  make export      - Export model to ONNX, TFLite, etc."
	@echo "  make api         - Run API server"
	@echo "  make ui          - Run Gradio UI"
	@echo "  make docs        - Generate documentation"
	@echo "  make docker      - Build Docker image"

# Initial setup
setup:
	@echo "Creating project directories..."
	mkdir -p configs/{model,training,inference}
	mkdir -p data/{raw,processed,interim,external}
	mkdir -p notebooks/{exploratory,preprocessing,model_development,results_analysis}
	mkdir -p scripts/{data_processing,training,evaluation,export,deployment}
	mkdir -p src/{data,models,training,utils,cli}
	mkdir -p api/{routes,models,services}
	mkdir -p ui/{components,pages}
	mkdir -p export
	mkdir -p evaluation/{metrics,visualizations,benchmarks}
	mkdir -p tests/{unit,integration,fixtures}
	mkdir -p weights/{pretrained,checkpoints}
	mkdir -p logs/{tensorboard,training,evaluation}
	mkdir -p docs
	@echo "Creating initial files..."
	touch README.md
	touch .env.example
	touch .gitignore
	@echo "Setup complete!"

# Virtual environment management
env:
	@echo "Creating virtual environment with uv..."
	uv venv

# Clean temporary files
clean:
	@echo "Cleaning temporary files and caches..."
	rm -rf __pycache__ .pytest_cache .coverage htmlcov
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Testing
test:
	@echo "Running tests..."
	pytest tests/

# Linting and formatting
lint:
	@echo "Running linters..."
	ruff check src/ tests/

format:
	@echo "Formatting code..."
	black src/ tests/
	isort src/ tests/

# Training
train:
	@echo "Starting model training..."
	python -m src.cli.main train --config configs/training/default.yaml

# Evaluation
eval:
	@echo "Evaluating model..."
	python -m src.cli.main evaluate --config configs/inference/default.yaml --weights weights/checkpoints/latest.pt

# Export
export:
	@echo "Exporting model..."
	python -m scripts.export.export_model --format onnx,tflite --weights weights/checkpoints/latest.pt --output export/

# API
api:
	@echo "Starting API server..."
	uvicorn api.app:app --reload --port 8000

# UI
ui:
	@echo "Starting Gradio UI..."
	python -m ui.app

# Documentation
docs:
	@echo "Generating documentation..."
	# Add your documentation generation command here
	# Example: mkdocs build

# Docker
docker:
	@echo "Building Docker image..."
	docker build -t ai-training-project .
