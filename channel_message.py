import telegram
import asyncio
import openAPI


response = openAPI.ChatGPT()

token = "6674460309:AAHk4cAmNaQK2zaqRzqmp58kQntILUJTCzs"

bot = telegram.Bot(token=token)
public_chat_name = '@jookbooinch'
id_channel = asyncio.run(bot.sendMessage(chat_id = public_chat_name ,
                        text= response))
print(id_channel)
