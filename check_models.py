import google.generativeai as genai

# PASTE YOUR KEY HERE
API_KEY = "AIzaSyDbruj6trqoWS5NmNZn1hj1yMrYZVvKKds"
genai.configure(api_key=API_KEY)

print("Available Models for your key:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")