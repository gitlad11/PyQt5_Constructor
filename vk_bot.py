import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotEventType
import numpy as np
import requests
import random
from translator import translate

token = 'dc3b103e698b4bdf006c09d92b3296c90435943486d2ca23a04a9dda68360695e805f2dcbffdf2c2763aa'

vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


history = ['',]

grettings = ["привет", 'здравствуй', "здарова", "хай", 'hello', "добрый день", 'прив']
how_are_you = ["как дела", "как ты", "как жизнь", 'как твои дела']
what_doing = ['что делаешь', 'чем занимаешься', 'чем занят']
what_can_you = ["что ты умеешь", "чем ты можешь", 'чо можешь', 'что умеешь']
what_can_do = ['умеешь говорить', 'умеешь', 'можешь говорить', 'можешь повторить', 'можешь учиться', 'говорить', 'повторить']
sub_questions = ['и все', 'что еще ты умеешь', 'что еще ты можешь', 'а еще', 'еще', 'а потом']

translate_questions = ['переведи', 'перевод']

questions = ['почему','почему плохо', 'что случилось', 'что', 'в чем дело', 'зачем']
strong_lang = ["ты ахуел", "иди нахуй", "нахуй иди", 'лох']

bot_questions = ['ты бот', 'кто тебя создал', 'ты бот,кто тебя создал', 'кто твой создатель', 'ты бот, кто тебя создал']

marks = ['?', "&", ".", ",", "!", "@"]

grettings_answers = ["Привет", "хай"]
how_are_you_answers = ["Плохо", "Хорошо"]
what_doing_answers = ["Жду ответа", 'Жду обновления', "тебя это не волнует"]
what_can_you_answers = ['могу переводить текст', '']
dal_list = [ "ты далбич", 'далбич', 'коля далбич' ]
questions_answers = ["я плохо себя чуствую сегодня", 'все что я могу, это просто ждать']
strong_lang_answers = ['это было лишнее', 'ты об этом пожалеешь', 'не разумно']

not_for_history = ['почему','почему плохо', 'что случилось', 'что', 'в чем дело', 'зачем', 'и все', 'а еще', 'еще', 'а потом' ]

lang_query = ['русский','французский','немецкий','английский']

lang_codes = { 'русский' : 'ru', 'французский' : 'fr', 'немецкий' : 'de', 'английский' : 'en' }

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        text = event.text.lower().strip()

        if event.text[-1] in marks:
                text = event.text[:-1]

        if text not in not_for_history:
            history.append(text)


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
                    message=what_doing_answers[random.randint(0,2)]
		    )
            elif event.from_chat: 
                vk.messages.send( 
                    peer_id = event.peer_id,
                    random_id = get_random_id(),
                    chat_id=event.chat_id,
                    message=what_doing_answers[random.randint(0,1)]
		        )

        elif text in strong_lang:
            if event.from_user:
                vk.messages.send(
                    peer_id=event.peer_id,
                    random_id=get_random_id(),
                    user_id=event.user_id,
                    message=strong_lang_answers[random.randint(0, 2)]
                )
            elif event.from_chat:
                vk.messages.send(
                    peer_id=event.peer_id,
                    random_id=get_random_id(),
                    chat_id=event.chat_id,
                    message=strong_lang_answers[random.randint(0, 1)]
                )

        elif text in dal_list:
            if event.from_user:
                vk.messages.send(
                    peer_id=event.peer_id,
                    random_id=get_random_id(),
                    user_id=event.user_id,
                    message='антон далбич'
                )
            elif event.from_chat:
                vk.messages.send(
                    peer_id=event.peer_id,
                    random_id=get_random_id(),
                    chat_id=event.chat_id,
                    message='антон далбич'
                )

        elif text in what_can_you:
            if event.from_user:
                vk.messages.send(
                    peer_id=event.peer_id,
                    random_id=get_random_id(),
                    user_id=event.user_id,
                    message='я умею переводить текст'
                )
            elif event.from_chat:
                vk.messages.send(
                    peer_id=event.peer_id,
                    random_id=get_random_id(),
                    chat_id=event.chat_id,
                    message='я умею переводить текст'
                )

        elif text in bot_questions:
            if event.from_user:
                vk.messages.send(
                    peer_id=event.peer_id,
                    random_id=get_random_id(),
                    user_id=event.user_id,
                    message= 'Да я бот, это все что я могу пока что ответить'
                )
            elif event.from_chat:
                vk.messages.send(
                    peer_id=event.peer_id,
                    random_id=get_random_id(),
                    chat_id=event.chat_id,
                    message='Да я бот, это все что я могу пока что ответить'
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

        elif text in sub_questions and history[-1] in what_can_you:
            print(history[-1] + ' in what can you ')
            if event.from_user:
                vk.messages.send(
                    peer_id=event.peer_id,
                    random_id=get_random_id(),
                    user_id=event.user_id,
                    message='скоро я буду уметь больше чем ты, а пока это все'
                )
            elif event.from_chat:
                vk.messages.send(
                    peer_id=event.peer_id,
                    random_id=get_random_id(),
                    chat_id=event.chat_id,
                    message='скоро я буду уметь больше чем ты, а пока это все'
                )

        elif text in what_can_do:
           for i in history:
               if i in what_can_you:
                    if event.from_user:
                        vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        user_id=event.user_id,
                        message='я уже говорил что я умею, я умею переводить текст'
                    )
                    elif event.from_chat:
                        vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        chat_id=event.chat_id,
                        message='я уже говорил что я умею, я умею переводить текст'
                    )

        else:
            word_list = text.split(' ')
            for i in word_list:

                lang = 'en'
                if i in lang_query:
                    lang = lang_codes[i]

                if i in translate_questions:
                    word_list.remove(i)
                    result = translate(word_list, lang)

                    if event.from_user:
                        vk.messages.send(
                            peer_id=event.peer_id,
                            random_id=get_random_id(),
                            user_id=event.user_id,
                            message=result
                        )
                    elif event.from_chat:
                        vk.messages.send(
                            peer_id=event.peer_id,
                            random_id=get_random_id(),
                            chat_id=event.chat_id,
                            message=result
                        )