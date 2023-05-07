from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)


trainer.train([
    "what is binary search",
    "Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.",
    ])


trainer.train([
    "who is elon musk",
    "A human being",
     
    ])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"jupiter: {chatbot.get_response(query)}")

    