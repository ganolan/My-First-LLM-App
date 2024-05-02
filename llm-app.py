import cohere

# Sign up for Cohere at https://dashboard.cohere.ai/signup
# Create an API key at https://dashboard.cohere.ai/api-keys
# Paste your Cohere API key in between the quotes below.
co = cohere.Client('insert apikey')

response = co.chat(
  chat_history=[
    {"role": "USER", "text": "hi"}, # Can also use "message" instead of "text"
    {"role": "CHATBOT", "text": "hi im fred"}
  ],
  message="whats your name?",
  # perform web search before answering the question. You can also use your own custom connector.
  connectors=[{"id": "web-search"}] 
)

# print the response
print(response.text)