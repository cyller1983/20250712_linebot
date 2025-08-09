from google import genai

# The client gsts the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="如何訓練地端ai模型?"
)
print(response.text)