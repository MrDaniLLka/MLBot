import vk_api 
from vk_api.longpoll import VkLongPoll, VkEventType
from config import tkn
import pickle
import os

session = vk_api.VkApi(token = tkn)
longpoll =  VkLongPoll(session)

vk_session = session.get_api()

clf = pickle.load(open(os.path.join('model.pkl'), 'rb'))

print("starting bot")
def Send(id, text):
    session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.from_chat and event.to_me:
        id = event.chat_id
        message = event.text.lower()
        name = event.chat_id
        if clf.predict([message]) == [1]:            
            Send(id, f'https://vk.com/id{event.user_id}, не ругайтесь')