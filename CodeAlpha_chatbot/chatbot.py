def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi! 😊"
    elif user_input == "how are you":
        return "I'm fine, thanks for asking! 😊"
    elif user_input == "bye":
        return "Goodbye! Have a nice day 👋"
    else:
        return "Sorry, I don't understand that."
print("🤖 Chatbot Started!")
print("Type 'bye' to exit.\n")

while True:
    user_message = input("You: ")

    reply = chatbot_response(user_message)
    print("Bot:", reply)

    if user_message.lower() == "bye":
        break
