from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot(
    'Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters = [
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter']
    )

trainer = ListTrainer(bot)

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de programar?', 'Sim, eu programo em Python']

bot.train(conversa)

name = input("Qual o seu nome? ")
print("Boas vindas ao serviço de bot!")
while True:
    try:
        request = input(name+ ': ')
        if request == 'Tchau' or request == 'tchau':
            print("Bot: Tchau")
            break
        else:
            response = bot.get_response(request)
            print('Bot:', response)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break