# Toon LLM Setup and Usage

## Prerequisites

### 1. Install Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Pull the gemma3:1b Model
```bash
ollama pull gemma3:1b
```

## Setup

### 1. Create Virtual Environment
```bash
python3 -m venv test
```

### 2. Activate Virtual Environment
```bash
source test/bin/activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

## Running the Script

Make sure Ollama is running, then execute:
```bash
python3 toon-llm.py
```
