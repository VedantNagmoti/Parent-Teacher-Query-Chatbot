import google.generativeai as genai

API_KEY = "[Paste your API key here]"
genai.configure(api_key=API_KEY)

print("Available Models for your key:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")
