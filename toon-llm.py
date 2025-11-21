import ollama
import json
from toon_format import encode, compare_formats

# 1. Your Raw Data (e.g., from a database query)
pc_parts_data = [
    {"sku": "CPU-01", "name": "Ryzen 7 7800X3D", "type": "CPU", "price": 449.00, "in_stock": True},
    {"sku": "GPU-02", "name": "NVIDIA RTX 4070 Super", "type": "GPU", "price": 599.99, "in_stock": True},
    {"sku": "GPU-03", "name": "Radeon RX 7800 XT", "type": "GPU", "price": 499.00, "in_stock": True},
    {"sku": "RAM-04", "name": "G.Skill Trident 32GB", "type": "RAM", "price": 115.00, "in_stock": False},
    {"sku": "MOBO-05", "name": "MSI B650 Tomahawk", "type": "Motherboard", "price": 219.99, "in_stock": True},
    {"sku": "PSU-06", "name": "Corsair RM850x", "type": "Power Supply", "price": 129.99, "in_stock": True}
]

# 2. See the Savings Immediately
# The library has a built-in comparison tool that shows JSON vs TOON side-by-side!
print("--- 📊 FORMAT EFFICIENCY REPORT ---")
print(compare_formats(pc_parts_data))
print("-" * 50)

# 3. Encode Data for the LLM
toon_payload = encode(pc_parts_data)

# 4. Chat with Ollama
print("\n🤖 Sending request to Gemma3...")
response = ollama.chat(model='gemma3:1b', messages=[
    {
        'role': 'system',
        'content': (
            "You are a PC building expert. "
            "Data is provided in TOON format (tabular). "
            "Use the data to answer user questions."
        )
    },
    {
        'role': 'user',
        'content': f"Here is the current inventory:\n\n{toon_payload}\n\n"
                   "Question: I have a budget of $550 for a graphics card (GPU). "
                   "Which one should I buy based on the price list, and is it in stock?"
    }
])

print("\n--- LLM RESPONSE ---")
print(response['message']['content'])