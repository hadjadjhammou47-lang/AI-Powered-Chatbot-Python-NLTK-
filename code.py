import random
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r"hi|hello", ["Hello!", "Hi there!"]),
    (r"how are you?", ["I'm good, thank you!", "Doing well, and you?"]),
    (r"(.*) your name?", ["I am a chatbot created by a CS student."]),
    (r"quit", ["Goodbye!", "See you later!"])
]

chatbot = Chat(pairs, reflections)
print("Chatbot ready! Type 'quit' to exit.")
chatbot.converse()
