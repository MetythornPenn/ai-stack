#!/usr/bin/env python3
"""
AI Training Project Generator

This script generates a complete project structure for AI training,
including directories and essential files with their content.
"""

import os
import sys
import shutil
import argparse
from pathlib import Path

# Project root
PROJECT_NAME = "ai-training-project"

def create_directory(path):
    """Create a directory if it doesn't exist"""
    os.makedirs(path, exist_ok=True)

def create_file(path, content=""):
    """Create a file with content"""
    with open(path, 'w') as f:
        f.write(content)

def create_readme(path, title):
    """Create a README.md file in a directory"""
    with open(os.path.join(path, "README.md"), 'w') as f:
        f.write(f"# {title}\n\nThis directory is used for {title.lower()}.\n")

def create_keep_file(path):
    """Create a .keep file in a directory to preserve it in Git"""
    open(os.path.join(path, ".keep"), 'w').close()

def main():
    parser = argparse.ArgumentParser(description="Generate AI Training Project Structure")
    parser.add_argument("--output", type=str, default=".", 
                        help="Output directory for the project structure")
    parser.add_argument("--name", type=str, default=PROJECT_NAME, 
                        help="Project name")
    args = parser.parse_args()
    
    # Project directory
    project_dir = os.path.join(args.output, args.name)
    
    # Ask for confirmation if directory exists
    if os.path.exists(project_dir):
        response = input(f"Directory {project_dir} already exists. Overwrite? [y/N]: ")
        if response.lower() != 'y':
            print("Operation canceled.")
            return
    
    # Create project directory
    create_directory(project_dir)
    print(f"Creating project structure in {project_dir}...")
    
    # Create main directories
    directories = [
        "configs/model",
        "configs/training",
        "configs/inference",
        "data/raw",
        "data/processed",
        "data/interim",
        "data/external",
        "notebooks/exploratory",
        "notebooks/preprocessing",
        "notebooks/model_development",
        "notebooks/results_analysis",
        "scripts/data_processing",
        "scripts/training",
        "scripts/evaluation",
        "scripts/export",
        "scripts/deployment",
        "src/data",
        "src/models/architectures",
        "src/models/components",
        "src/training",
        "src/utils",
        "src/cli",
        "api/routes",
        "api/models",
        "api/services",
        "ui/components",
        "ui/pages",
        "export",
        "evaluation/metrics",
        "evaluation/visualizations",
        "evaluation/benchmarks",
        "tests/unit",
        "tests/integration",
        "tests/fixtures",
        "weights/pretrained",
        "weights/checkpoints",
        "logs/tensorboard",
        "logs/training",
        "logs/evaluation",
        "docs",
    ]
    
    for directory in directories:
        full_path = os.path.join(project_dir, directory)
        create_directory(full_path)
        create_keep_file(full_path)  # Add .keep file to all directories
    
    print("✓ Created directories with .keep files")
    
    # Create README files
    for directory in [
        "data/raw",
        "data/processed",
        "data/interim",
        "data/external",
        "weights/pretrained",
        "weights/checkpoints",
        "logs/tensorboard",
        "logs/training",
        "logs/evaluation",
    ]:
        create_readme(os.path.join(project_dir, directory), directory.split('/')[-1].capitalize())
    
    print("✓ Created README files for data directories")
    
    # Create empty __init__.py files
    init_py_dirs = [
        "src",
        "src/data",
        "src/models",
        "src/models/architectures",
        "src/models/components",
        "src/training",
        "src/utils",
        "src/cli",
        "api",
        "api/routes",
        "api/models",
        "api/services",
        "ui",
        "ui/components",
        "ui/pages",
        "export",
        "evaluation",
        "tests",
        "tests/unit",
        "tests/integration",
    ]
    
    for directory in init_py_dirs:
        create_file(os.path.join(project_dir, directory, "__init__.py"))
    
    print("✓ Created __init__.py files")
    
    # Create pyproject.toml file
    create_file(os.path.join(project_dir, "pyproject.toml"), """[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pyi?$'

[tool.isort]
profile = "black"
multi_line_output = 3

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
""")
    
    # Create a simple makefile with uv support
    create_file(os.path.join(project_dir, "Makefile"), """
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
""")
    
    # Create a detailed README.md
    create_file(os.path.join(project_dir, "README.md"), f"""# {args.name}

A comprehensive project structure for AI model development, training, evaluation, and deployment.

## Project Structure

This repository provides a well-organized structure for developing AI projects:

```
ai-training-project/
├── configs/       # Configuration files
├── data/          # Dataset storage
├── notebooks/     # Jupyter notebooks
├── scripts/       # Utility scripts
├── src/           # Main source code
├── api/           # API implementation
├── ui/            # Gradio UI
├── export/        # Model export utilities
├── evaluation/    # Evaluation code
├── tests/         # Test suite
├── weights/       # Model weights
├── logs/          # Training logs
└── docs/          # Documentation
```

## Getting Started

### Prerequisites

- Python 3.8+
- uv package manager

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/{args.name}.git
   cd {args.name}
   ```

2. Set up the project structure:
   ```bash
   make setup
   ```

3. Create a virtual environment and install dependencies using uv:
   ```bash
   uv venv
   source .uv/env/bin/activate  # On Windows: .uv\\env\\Scripts\\activate
   ```

4. Install required packages:
   ```bash
   uv pip install numpy pandas scikit-learn matplotlib
   uv pip install torch torchvision
   uv pip install fastapi uvicorn gradio
   uv pip install pytest black isort ruff
   ```

## Usage

The Makefile provides shortcuts for common operations:

### Development

- **Setup project structure**: `make setup`
- **Run tests**: `make test`
- **Format code**: `make format`
- **Run linters**: `make lint`
- **Clean temporary files**: `make clean`

### Training and Evaluation

- **Train a model**: `make train`
- **Evaluate a model**: `make eval`
- **Export a model**: `make export`

### Deployment

- **Run API server**: `make api`
- **Run Gradio UI**: `make ui`

## Configuration

The project uses YAML configuration files located in the `configs/` directory:

- `configs/model/` - Model architecture configurations
- `configs/training/` - Training configurations
- `configs/inference/` - Inference configurations

Example:

```yaml
# configs/training/default.yaml
project:
  name: "ai_training_project"
  
data:
  dataset: "custom_dataset"
  batch_size: 32

model:
  architecture: "resnet50"
  num_classes: 10

training:
  epochs: 100
  optimizer:
    name: "adam"
    learning_rate: 0.001
```

## Data Management

Place your datasets in the appropriate directories:

- `data/raw/` - Raw, unprocessed data
- `data/processed/` - Processed, ready-to-use data
- `data/interim/` - Intermediate data processing results
- `data/external/` - External data sources

## Model Development

1. Define your model architecture in `src/models/`
2. Implement data loading in `src/data/`
3. Configure training in `configs/`
4. Run training with `make train`

## Evaluation and Export

1. Evaluate your model with `make eval`
2. Export your model to different formats:
   ```bash
   python scripts/export/export_model.py --weights weights/checkpoints/model.pt --format onnx,tflite
   ```

## API and UI

- Start the FastAPI server: `make api`
- Start the Gradio UI: `make ui`

The API server will be available at http://localhost:8000 with documentation at http://localhost:8000/docs.

## Adding New Components

### Adding a New Model

1. Create a new file in `src/models/architectures/`
2. Implement the model class
3. Register the model in `src/models/__init__.py`
4. Create a configuration in `configs/model/`

### Adding a New Dataset

1. Create a new dataset class in `src/data/dataset.py`
2. Implement data loading and preprocessing
3. Update the data configuration in `configs/training/`

## Project Organization

    ├── LICENSE            <- License file
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project
    ├── configs/           <- Configuration files
    │   ├── model/         <- Model configurations
    │   ├── training/      <- Training configurations
    │   └── inference/     <- Inference configurations
    │
    ├── data/              <- Data storage
    │   ├── raw/           <- The original, immutable data dump
    │   ├── processed/     <- The final, canonical data sets for modeling
    │   ├── interim/       <- Intermediate data that has been transformed
    │   └── external/      <- Data from third party sources
    │
    ├── notebooks/         <- Jupyter notebooks
    │   ├── exploratory/   <- Initial data exploration
    │   ├── preprocessing/ <- Data preprocessing notebooks
    │   ├── model_development/ <- Model development and experimentation
    │   └── results_analysis/  <- Analysis of results
    │
    ├── scripts/           <- Utility scripts
    │   ├── data_processing/ <- Scripts for data processing
    │   ├── training/      <- Scripts for training models
    │   ├── evaluation/    <- Scripts for model evaluation
    │   ├── export/        <- Scripts for model export
    │   └── deployment/    <- Scripts for model deployment
    │
    ├── src/               <- Source code for use in this project
    │   ├── __init__.py    <- Makes src a Python package
    │   ├── data/          <- Code to process data
    │   ├── models/        <- Model implementations
    │   ├── training/      <- Training implementations
    │   ├── utils/         <- Utility functions
    │   └── cli/           <- Command line interface
    │
    ├── api/               <- API implementation (FastAPI)
    │   ├── app.py         <- Main API application
    │   ├── routes/        <- API routes
    │   ├── models/        <- API models (Pydantic)
    │   └── services/      <- Business logic services
    │
    ├── ui/                <- UI implementation (Gradio)
    │   ├── app.py         <- Main UI application
    │   ├── components/    <- UI components
    │   └── pages/         <- UI pages
    │
    ├── export/            <- Code for model export
    │
    ├── evaluation/        <- Code for model evaluation
    │   ├── metrics/       <- Evaluation metrics
    │   ├── visualizations/ <- Evaluation visualizations
    │   └── benchmarks/    <- Benchmarking tools
    │
    ├── tests/             <- Test files
    │   ├── unit/          <- Unit tests
    │   ├── integration/   <- Integration tests
    │   └── fixtures/      <- Test fixtures
    │
    ├── weights/           <- Model weights
    │   ├── pretrained/    <- Pretrained weights
    │   └── checkpoints/   <- Training checkpoints
    │
    ├── logs/              <- Log files
    │   ├── tensorboard/   <- TensorBoard logs
    │   ├── training/      <- Training logs
    │   └── evaluation/    <- Evaluation logs
    │
    └── docs/              <- Documentation
""")
    
    # Create a simple config file for training
    create_file(os.path.join(project_dir, "configs/training/default.yaml"), """# Config file for model training
# configs/training/default.yaml

# General settings
project:
  name: "ai_training_project"
  version: "0.1.0"
  description: "AI training project with configurable parameters"
  seed: 42

# Data settings
data:
  dataset: "custom_dataset"  # Name of the dataset
  train_path: "data/processed/train"
  val_path: "data/processed/val"
  test_path: "data/processed/test"
  batch_size: 32
  num_workers: 4
  
  # Data preprocessing
  preprocessing:
    image_size: [224, 224]
    normalize: true
    mean: [0.485, 0.456, 0.406]  # ImageNet mean
    std: [0.229, 0.224, 0.225]   # ImageNet std
  
  # Data augmentation
  augmentation:
    enabled: true
    horizontal_flip: true
    vertical_flip: false
    rotation_range: 15
    brightness_range: [0.8, 1.2]
    contrast_range: [0.8, 1.2]

# Model settings
model:
  name: "custom_model"
  architecture: "resnet50"  # Base architecture
  pretrained: true  # Use pretrained weights
  num_classes: 10
  dropout_rate: 0.2
  activation: "relu"
  
  # Model-specific parameters
  params:
    embed_dim: 256
    depth: 4
    num_heads: 8

# Training settings
training:
  epochs: 100
  early_stopping:
    enabled: true
    patience: 10
    min_delta: 0.001
  
  # Optimizer
  optimizer:
    name: "adam"
    learning_rate: 0.001
    weight_decay: 0.0001
    beta1: 0.9
    beta2: 0.999
  
  # Learning rate scheduler
  lr_scheduler:
    name: "cosine"
    warmup_epochs: 5
    min_lr: 0.00001
  
  # Loss function
  loss:
    name: "cross_entropy"
    label_smoothing: 0.1
  
  # Gradient settings
  gradient:
    clip_norm: 1.0
    accumulation_steps: 1

# Callbacks and logging
callbacks:
  checkpoint:
    save_best_only: true
    save_frequency: 5  # Save every N epochs
    
  tensorboard:
    enabled: true
    log_dir: "logs/tensorboard"
    
  csv_logger:
    enabled: true
    path: "logs/training/metrics.csv"

# Evaluation settings
evaluation:
  metrics: ["accuracy", "precision", "recall", "f1"]
  confusion_matrix: true
  
# Export settings
export:
  formats: ["onnx", "tflite", "torchscript"]
  quantization: true
  optimize: true
""")
    
    # Create a simple config file for inference
    create_file(os.path.join(project_dir, "configs/inference/default.yaml"), """# Config file for inference
# configs/inference/default.yaml

# General settings
project:
  name: "ai_training_project"
  version: "0.1.0"
  description: "AI training project inference configuration"

# Model settings
model:
  name: "custom_model"
  architecture: "resnet50"
  num_classes: 10
  checkpoint_path: "weights/checkpoints/latest.pt"

# Input settings
input:
  shape: [1, 3, 224, 224]  # [batch_size, channels, height, width]
  normalize: true
  mean: [0.485, 0.456, 0.406]  # ImageNet mean
  std: [0.229, 0.224, 0.225]   # ImageNet std

# Inference settings
inference:
  batch_size: 1
  device: "cuda"  # "cuda" or "cpu"
  precision: "fp32"  # "fp32", "fp16", or "int8"
  threshold: 0.5  # Confidence threshold for predictions

# API settings
api:
  host: "0.0.0.0"
  port: 8000
  workers: 4
  timeout: 60
""")
    
    # Create a simple .gitignore file
    create_file(os.path.join(project_dir, ".gitignore"), """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
.python-version
.uv/

# IDE
.idea/
.vscode/
*.swp
*.swo
.DS_Store

# Jupyter Notebook
.ipynb_checkpoints

# Project specific
logs/
weights/
!weights/pretrained/README.md
!weights/checkpoints/README.md
!weights/pretrained/.keep
!weights/checkpoints/.keep
data/raw/*
data/processed/*
data/interim/*
data/external/*
!data/raw/README.md
!data/processed/README.md
!data/interim/README.md
!data/external/README.md
!data/raw/.keep
!data/processed/.keep
!data/interim/.keep
!data/external/.keep
""")
    
    print("\nProject structure created successfully!")
    print(f"\nTo get started, run:\n\ncd {args.name}")
    print("uv venv")
    print("source .uv/env/bin/activate  # On Windows: .uv\\env\\Scripts\\activate")
    print("uv pip install numpy pandas torch fastapi gradio # Install packages as needed")
    print("make help  # To see available commands")

if __name__ == "__main__":
    main()