import vk_api 
from vk_api.longpoll import VkLongPoll, VkEventType
from config import tkn

session = vk_api.VkApi(token = tkn)
longpoll =  VkLongPoll(session)

print("starting bot")
def Send(id, text):
    session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.from_chat and event.to_me:
        id = event.chat_id
        message = event.text.lower()
        Send(id, message)