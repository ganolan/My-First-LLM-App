import cohere

# Sign up for Cohere at https://dashboard.cohere.ai/signup
# Create an API key at https://dashboard.cohere.ai/api-keys
# Paste your Cohere API key in between the quotes below.
co = cohere.Client('Paste your Cohere API key here')

response = co.chat(
  chat_history=[
    {"role": "USER", "text": "Hi"}, # Can also use "message" instead of "text"
    {"role": "CHATBOT", "text": "Hi, I'm Hal."},
    {"role": "USER", "text": "Hi Hal, I want you to act as my personal tutor."},
    {"role": "USER", "text": "If I ask you a question do not give me the answer. Instead, guide me through the steps to find the answer myself."}
  ],
  message="A right angle triangle has two straight side lengths of 3 and 4. What is the length of the hypotenuse?",
  # perform web search before answering the question. You can also use your own custom connector.
  connectors=[{"id": "web-search"}] 
)

# print the response
print(response.text)