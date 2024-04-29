import cohere

co = cohere.Client('insert apikey')

response = co.chat(
  chat_history=[
    {"role": "USER", "message": "hi"},
    {"role": "CHATBOT", "message": "hi im fred"}
  ],
  message="whats your name?",
  # perform web search before answering the question. You can also use your own custom connector.
  connectors=[{"id": "web-search"}] 
)
print(response)