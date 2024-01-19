from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('SimpleBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language corpus data
trainer.train('chatterbot.corpus.english')

def chat_with_bot():
    print("Hello! I'm your SimpleBot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day.")
            break

        # Get the chatbot's response
        bot_response = chatbot.get_response(user_input)

        print(f"SimpleBot: {bot_response}")

if __name__ == "__main__":
    chat_with_bot()
