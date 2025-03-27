# ai-training-project

A comprehensive project structure for AI model development, training, evaluation, and deployment.

## Project Structure

This repository provides a well-organized structure for developing AI projects:

```
ai-training-project/
├── configs/       # Configuration files
├── data/          # Dataset storage
├── notebooks/     # Jupyter notebooks
├── performance/   # Loadtest API 
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
   git clone https://github.com/MetythornPenn/ai-stack.git konai
   cd konai
   ```

2. Create a virtual environment and install dependencies using uv:
   ```bash
   make env 
   # or 
   uv venv -p 3.10

   source .venv/env/bin/activate  # On Windows: .uv\env\Scripts\activate
   ```

3. Install required packages:
   ```bash
   make install
   # or 
   uv sync
   ```

## Usage

The Makefile provides shortcuts for common operations:

### Development

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
