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
Output
```shell
--- 📊 FORMAT EFFICIENCY REPORT ---
Format Comparison
────────────────────────────────────────────────
Format      Tokens    Size (chars)
JSON          301            764
TOON          132            310
────────────────────────────────────────────────
Savings: 169 tokens (56.1%)
--------------------------------------------------

🤖 Sending request to Gemma3...

--- LLM RESPONSE ---
Okay, let’s analyze this and recommend a GPU for you within your $550 budget.

Based on the provided inventory, the best option for a GPU is:

**GPU-02, NVIDIA RTX 4070 Super, GPU, 599.99, true**

**Is it in stock?** Yes, the inventory shows that GPU-02 is currently in stock.

**Recommendation:**

The NVIDIA RTX 4070 Super offers a fantastic balance of performance and price for your budget. It’s a solid choice for gaming at 1440p and will handle most games with reasonable settings.

To help me refine this further, could you tell me:

*   **What resolution and refresh rate are you planning to use?** (e.g., 1440p 144Hz, 1080p 60Hz)
*   **What games do you plan to play?** (e.g., Cyberpunk 2077, Fortnite, etc.)
```
