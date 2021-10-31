import vk_api 
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import tkn

session = vk_api.VkApi(token = tkn)
longpoll =  VkBotLongPoll(session, 208438501)
print("starting bot")
def Send(id, text):
    session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0})

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
        id = event.user_id
        message = event.text.lower()
        Send(id, 'COCK')