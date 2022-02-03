import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotEventType
import numpy as np
import requests
import random

token = 'dc3b103e698b4bdf006c09d92b3296c90435943486d2ca23a04a9dda68360695e805f2dcbffdf2c2763aa'

vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


history = ['',]

grettings = ["привет", 'здравствуй', "здарова", "хай", 'hello', "добрый день", 'прив']
how_are_you = ["как дела", "как ты", "как жизнь", ]
what_doing = ['что делаешь', 'чем занимаешься', 'чем занят']


questions = ['почему' ,'что случилось', 'что', 'в чем дело', 'зачем']

marks = ['?', "&", ".", ",", "!", "@"]

grettings_answers = ["Привет", "хай"]
how_are_you_answers = ["Плохо", "Хорошо"]
what_doing_answers = ["Жду ответа", "тебя это не волнует"]

questions_answers = ["я плохо себя чуствую сегодня", 'просто убиваю время']

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        text = event.text.lower().strip()
        if event.text[-1] in marks:
                text = event.text[:-1]

        if text not in questions:   
            history.append(text)

        print(history)

        if text in grettings:

            if event.from_user:
                vk.messages.send( 
                    peer_id = event.peer_id,
                    random_id = get_random_id(),
                    user_id=event.user_id,
                    message=grettings_answers[random.randint(0,1)]
		)
            elif event.from_chat: 
                vk.messages.send( 
                    peer_id = event.peer_id,
                    random_id = get_random_id(),
                    chat_id=event.chat_id,
                    message=grettings_answers[random.randint(0,1)]
		)

        elif text in how_are_you:
       
            if event.from_user:
                vk.messages.send( 
                    peer_id = event.peer_id,
                    random_id = get_random_id(),
                    user_id=event.user_id,
                    message=how_are_you_answers[random.randint(0,1)]
		    )
            elif event.from_chat: 
                vk.messages.send( 
                    peer_id = event.peer_id,
                    random_id = get_random_id(),
                    chat_id=event.chat_id,
                    message=how_are_you_answers[random.randint(0,1)]
		        )

        elif text in what_doing:
            if event.from_user:
                vk.messages.send( 
                    peer_id = event.peer_id,
                    random_id = get_random_id(),
                    user_id=event.user_id,
                    message=what_doing_answers[random.randint(0,1)]
		    )
            elif event.from_chat: 
                vk.messages.send( 
                    peer_id = event.peer_id,
                    random_id = get_random_id(),
                    chat_id=event.chat_id,
                    message=what_doing_answers[random.randint(0,1)]
		        )
        elif text in questions and history[-1] in how_are_you:
            if event.from_user:
                vk.messages.send( 
                    peer_id = event.peer_id,
                    random_id = get_random_id(),
                    user_id=event.user_id,
                    message=questions_answers[0]
		    )
            elif event.from_chat: 
                vk.messages.send( 
                    peer_id = event.peer_id,
                    random_id = get_random_id(),
                    chat_id=event.chat_id,
                    message=questions_answers[0]
		        )
        elif text in questions and history[-1] in what_doing:
            if event.from_user:
                vk.messages.send( 
                    peer_id = event.peer_id,
                    random_id = get_random_id(),
                    user_id=event.user_id,
                    message=questions_answers[1]
		    )
            elif event.from_chat: 
                vk.messages.send( 
                    peer_id = event.peer_id,
                    random_id = get_random_id(),
                    chat_id=event.chat_id,
                    message=questions_answers[1]
		        )
        elif text in questions and not history[-1] in what_doing or not history[-1] in how_are_you:
            if event.from_user:
                vk.messages.send( 
                    peer_id = event.peer_id,
                    random_id = get_random_id(),
                    user_id=event.user_id,
                    message= "что вы хотите узнать?"
		    )
            elif event.from_chat: 
                vk.messages.send( 
                    peer_id = event.peer_id,
                    random_id = get_random_id(),
                    chat_id=event.chat_id,
                    message= "что вы хотите узнать?"
		        )                  
                       