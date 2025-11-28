from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    'Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters = [
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter']
    )

trainer = ListTrainer(chatbot)

trainer.train([
    'Oi',
    'Olá',
    'Tudo bem?',
    'Tudo ótimo',
    'Você gosta de programar?',
    'Sim, eu programo em Python'
])

name = input("Qual o seu nome? ")
print("Boas vindas ao serviço de bot!")
while True:
    try:
        request = input(name+ ': ')
        if request == 'Tchau' or request == 'tchau':
            print("Bot: Tchau")
            break
        else:
            response = chatbot.get_response(request)
            print('Bot:', response)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break