from smolagents import LiteLLMModel
import requests

try:
    # Check if the Ollama server is running
    response = requests.get("http://127.0.0.1:11434")
    if response.status_code == 200:
        print("Ollama server is running.")
    else:
        print(f"Error: Unable to connect to Ollama server (Status code: {response.status_code})")
except requests.exceptions.RequestException as e:
    print(f"Error connecting to Ollama server: {e}")

try:
    model = LiteLLMModel(
        model_id="ollama_chat/qwen2.5:7b",  # Replace with your model
        api_base="http://127.0.0.1:11434",  # Default Ollama local server
        num_ctx=8192,
    )
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading the model: {e}")
