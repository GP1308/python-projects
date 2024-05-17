
                              #CHATBOT CREATED USING PYTHON

# Importing the random library 
import random

# Defining a dictionary with responses
responses = {
	"hello": ["Hello! How can I assist you today?", "Hi! What's on your mind?", "Hey! How's it going?", "Hello! I'm here to help with any questions or topics you'd like to discuss. What's on your mind?"],
	"hi": ["Hey! How's it going?", "Hello! What can I help you with?", "Hi! What's up?", "Hi there! I'm here to help with any questions or topics you'd like to discuss. How can I assist you today?"],
	"how are you": ["I'm doing well, thanks for asking!", "I'm good, how about you?", "I'm great, thanks for asking!", "I'm a large language model, so I don't have feelings like humans do, but I'm here to help you with any questions or topics you'd like to discuss."],
	"what is your name": ["My name is ChatBot!", "I'm ChatBot, nice to meet you!", "My name is ChatBot, what's yours?", "I don't have a personal name, but I'm here to assist you with any questions or topics you'd like to discuss. You can call me ChatBot for short."],
	"what can you do": ["I can answer any questions you have!", "I can assist with a variety of tasks!", "I can provide information on a wide range of topics!", "I can help with a wide range of tasks, such as answering questions, providing information, and generating text. I can also assist with more creative tasks, such as writing stories or generating ideas."],
	"default": ["I didn't quite understand that. Can you please rephrase?", "Sorry, I didn't catch that. Can you repeat?", "I'm not sure I understand. Can you please provide more context?", "I'm here to help, but I need a bit more information to provide a helpful response. Can you please provide more context or clarify your question?"],
	"tell me a joke": ["Why did the computer go to the doctor? It had a virus!", "Why did the scarecrow win an award? Because he was outstanding in his field!", "What do you call a fake noodle? An impasta!", "Why did the bicycle fall over? Because it was two-tired!"],
	"write a poem": ["Roses are red, violets are blue, I'm here to help, and so are you.", "The sun sets slow, the stars come out, I'm here to help, without a doubt.", "The world is vast, the world is wide, I'm here to help, with a helpful stride.", "The pen is mightier, than the sword they say, I'm here to help, in a helpful way."],
	"give me a fact": ["The shortest war in history was between Britain and Zanzibar on August 27, 1896, and lasted only 38 minutes.", "The longest word in the English language, according to the Oxford English Dictionary, is pneumonoultramicroscopicsilicovolcanoconiosis, a lung disease caused by inhaling very fine particles of silica.", "The highest mountain in the solar system is Olympus Mons on Mars, which is around three times the size of Mount Everest.", "The deepest part of the ocean is the Mariana Trench, which is over 36,000 feet deep."],
}

# Defining a function to get a response
def get_response(message):
	message = message.lower()
	for key in responses:
		if key in message:
			return random.choice(responses[key])
	return random.choice(responses["default"])

# Creating a chatbot
def chatbot():
	print("Welcome to the chatbot!")
	while True:
		message = input("You: ")
		response = get_response(message)
		print("Chatbot:", response)

chatbot()
