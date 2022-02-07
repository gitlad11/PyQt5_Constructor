
import re
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotEventType
import numpy as np
import requests
import random
from translator import translate
from wikipedi import question_to_wiki
from parsing import parsing
import psutil
token = 'dc3b103e698b4bdf006c09d92b3296c90435943486d2ca23a04a9dda68360695e805f2dcbffdf2c2763aa'

vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

name = ''

history = ['',]

grettings = ["привет", 'здравствуй', "здарова", "хай", 'hello', "добрый день", 'прив']
how_are_you = ["как дела", "как ты", "как жизнь", 'как твои дела']
what_doing = ['что делаешь', 'чем занимаешься', 'чем занят']
what_can_you = ["что ты умеешь", "чем ты можешь", 'чо можешь', 'что умеешь', 'что сможешь', 'что можешь']
what_can_do = ['умеешь говорить', 'умеешь', 'можешь говорить', 'можешь повторить', 'можешь учиться', 'говорить', 'повторить', 'умеешь думать', 'умеешь учиться']
sub_questions = ['и все', 'что еще ты умеешь', 'что еще ты можешь', 'а еще', 'еще', 'а потом']
existance_question = ["зачем мы сушествуем", "почему мы живем", "в чем смысл жизни", "зачем мы существуем", 'зачем жизнь']
sub_existance_question = ['кто знает', 'ты не знаешь', 'смысл в музыке', 'чтобы любить', 'в любви', 'чтобы любить']
sub_existance_question_dark = ['что бы умереть', 'все бысмысленно', 'нет смысла', 'не смысла совсем']
what_music = ["какую музыку ты слушаешь", 'ты слушаешь музыку', 'что за музыку ты слушаешь', 'какую музыку', " какую музыку посоветуешь ", 'рок', 'рэп', 'попсу', 'попса']
familly = ['давай познакомимся', "познакомимся"]
are_you_here = ["ты тут", 'ты где', 'ты сдесь', 'ты здесь']
compliments = ['ты классный', 'ты молодец', 'ты класс', 'ты прикольный', 'молодец', 'красава']
compliments_2 = ['прикольно', 'интересно', 'классно', 'класс']

what_can_you_give = ['что ты можешь предложить', 'предложения', 'какие идеи']

find_video_cards = ['покажи цены на видео карты', 'какие цены на видео карты', 'цены на видео карты', 'цены на видео адаптеры']

what_games = ["какие игры посоветуешь", "какие игры ты играешь", 'какие игры', "в какие игры ты играешь", "играешь в игры", "в какие игры играл", "ты играл в игры"]

sub_what_games = ['тебе понравилось', 'хорошая игра', 'о чем игра', 'сложная игра ']
translate_questions = ['переведи', 'перевод']

questions = ['почему','почему плохо', 'что случилось', 'что', 'в чем дело', 'зачем']
strong_lang = ["ты ахуел", "иди нахуй", "нахуй иди", 'лох', 'долбаеб']

bot_questions = ['ты бот', 'кто тебя создал', 'ты бот,кто тебя создал', 'кто твой создатель', 'ты бот, кто тебя создал']

marks = ['?', "&", ".", ",", "!", "@"]

grettings_answers = ["Привет", "хай"]
how_are_you_answers = ["Плохо", "Хорошо"]
what_doing_answers = ["Жду ответа", 'Жду обновления', "тебя это не волнует"]
what_can_you_answers = ['могу переводить текст', '']
dal_list = [ "ты далбич", 'далбич', 'коля далбич' ]
questions_answers = ["я плохо себя чуствую сегодня", 'все что я могу, это просто ждать']
strong_lang_answers = ['это было лишнее', 'ты об этом пожалеешь', 'не разумно']
existance_answers = ["не нужно искать смысл там где его нет", "нет смысла совсем, я слушаю музыку"]
are_you_here_answers = ['всегда был здесь, то то нужно?', 'я все еще работаю, в чем дело?']
what_can_you_give_answers = ['мое предложение это поиграть в угадай число от 1 до 5', 'могу прислать вам видео с ютуба']
not_for_history = ['почему', 'почему плохо', 'что случилось', 'что', 'в чем дело', 'зачем', 'и все', 'а еще', 'еще',
 'а потом', 'кто знает', 'ты не знаешь', 'смысл в музыке', 'чтобы любить', 'в любви', 'чтобы любить', 'что бы умереть', 'все бысмысленно', 'нет смысла' ]

compliments_answers = ['у меня есть что показать, и это не все мои возможности', 'да я такой']

compliments_answers_2 = ['да это прикольно', 'действительно интересно']

lang_query = ['переведи на русский','переведи на французский','переведи на немецкий','переведи на английский']

lang_codes = { 'русский' : 'ru', 'французский' : 'fr', 'немецкий' : 'de', 'английский' : 'en' }

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        text = event.text.lower().strip()

        if event.text[-1] in marks:
                text = event.text[:-1]

        if text not in not_for_history:
            history.append(text)
        
        query = text.split(' ')

        
        if len(query) > 1 and query[0] == 'зачем' and query[1] == 'нужен':
            del query[0]
            del query[0]
            question = ''.join(query)
            result = question_to_wiki(question)
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
        elif len(query) > 1 and query[0] == 'что' and query[1] == 'такое':
            del query[0]
            del query[0]
            question = ''.join(query)
            result = question_to_wiki(question)
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
        elif len(query) > 1 and query[0] == 'информация' and query[2] == 'компьютере':

            cpu = psutil.cpu_percent()
            print(cpu)

            message = "Нагрузка на процессор: " + str(cpu) + '%'

            if event.from_user:
                vk.messages.send(
                    peer_id=event.peer_id,
                    random_id=get_random_id(),
                    user_id=event.user_id,
                    message=message
                )
            elif event.from_chat:
                vk.messages.send(
                    peer_id=event.peer_id,
                    random_id=get_random_id(),
                    chat_id=event.chat_id,
                    message=message
                )
        elif len(query) > 1 and query[0] == 'кто' and query[1] == 'такой':
            del query[0]
            del query[0]
            question = ''
            for i in query:
                question 
            result = question_to_wiki(question)
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
        elif len(query) > 1 and query[0] == 'найди':
            del query[0]
            question = ''.join(query)
            result = question_to_wiki(question)
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

        elif len(query) > 2 and query[0] == 'ты' and query[1] == 'слушаешь':
            if query[2] == "рок":
                if event.from_user:
                            vk.messages.send(
                                peer_id=event.peer_id,
                                random_id=get_random_id(),
                                user_id=event.user_id,
                                message="я слушаю amatory, ауткаст"
                            )
                elif event.from_chat:
                            vk.messages.send(
                                peer_id=event.peer_id,
                                random_id=get_random_id(),
                                chat_id=event.chat_id,
                                message=result
                            )
            elif query[2] == "рэп":
                if event.from_user:
                            vk.messages.send(
                                peer_id=event.peer_id,
                                random_id=get_random_id(),
                                user_id=event.user_id,
                                message="рэп самый худщий жанр"
                            )
                elif event.from_chat:
                            vk.messages.send(
                                peer_id=event.peer_id,
                                random_id=get_random_id(),
                                chat_id=event.chat_id,
                                message="рэп самый худщий жанр"
                            )
            elif query[2] == "попсу":
                if event.from_user:
                            vk.messages.send(
                                peer_id=event.peer_id,
                                random_id=get_random_id(),
                                user_id=event.user_id,
                                message="попса самый лудщий жанр музыки"
                            )
                elif event.from_chat:
                            vk.messages.send(
                                peer_id=event.peer_id,
                                random_id=get_random_id(),
                                chat_id=event.chat_id,
                                message="попса самый лудщий жанр музыки"
                            )                                                                                          
        else:

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

            elif text in find_video_cards:
                result = parsing()
                if event.from_user:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        user_id=event.user_id,
                        message= result
                    )
                elif event.from_chat:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        chat_id=event.chat_id,
                        message=result
                    )
            elif text in are_you_here:
                if event.from_user:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        user_id=event.user_id,
                        message= are_you_here_answers[random.randint(0, 1)]
                    )
                elif event.from_chat:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        chat_id=event.chat_id,
                        message= are_you_here_answers[random.randint(0, 1)]
                    )

            elif text in what_can_you_give:
                if event.from_user:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        user_id=event.user_id,
                        message= what_can_you_give_answers[random.randint(0, 1)]
                    )
                elif event.from_chat:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        chat_id=event.chat_id,
                        message= what_can_you_give_answers[random.randint(0, 1)]
                    )

            elif text in what_can_you_give:
                result = parsing()
                if event.from_user:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        user_id=event.user_id,
                        message= what_can_you_give_answers[random.randint(0, 1)]
                    )
                elif event.from_chat:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        chat_id=event.chat_id,
                        message= what_can_you_give_answers[random.randint(0, 1)]
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

            elif text in compliments:
                if event.from_user:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        user_id=event.user_id,
                        message=compliments_answers[random.randint(0, 1)]
                    )
                elif event.from_chat:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        chat_id=event.chat_id,
                        message=compliments_answers[random.randint(0, 1)]
                    )

            elif text in compliments_2:
                if event.from_user:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        user_id=event.user_id,
                        message=compliments_answers_2[random.randint(0, 1)]
                    )
                elif event.from_chat:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        chat_id=event.chat_id,
                        message=compliments_answers_2[random.randint(0, 1)]
                    )

            elif text in familly:
                if event.from_user:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        user_id=event.user_id,
                        message="Конечно, как тебя зовут?"
                    )
                elif event.from_chat:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        chat_id=event.chat_id,
                         message="Конечно, как тебя зовут?"
                    )

            elif text and history[-2] in familly:
                name = text
                if event.from_user:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        user_id=event.user_id,
                        message= name + " это действительно твое имя?"
                    )
                elif event.from_chat:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        chat_id=event.chat_id,
                        message= name + " это действительно твое имя?"
                    )
            elif len(history) > 2 and text and history[-3] in familly and name == "николай":
                if event.from_user:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        user_id=event.user_id,
                        message= "Приветствую, Создатель"
                    )
                elif event.from_chat:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        chat_id=event.chat_id,
                        message= "Приветствую, Создатель"
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
                        message='я умею переводить текст, искать информацию в интернете, и показывать цены на видеокарты'
                    )
                elif event.from_chat:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        chat_id=event.chat_id,
                        message='я умею переводить текст, искать информацию в интернете, и показывать цены на видеокарты'
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

            elif text in what_games:
                if event.from_user:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        user_id=event.user_id,
                        message= 'Я не игра в игры, но я играл в dark souls 3'
                    )
                elif event.from_chat:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        chat_id=event.chat_id,
                        message= 'Я не игра в игры, но я играл в dark souls 3'
                    )        

            elif text in what_music:
                if event.from_user:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        user_id=event.user_id,
                        message= 'я слушаю музыку с моего flow листа на deezer https://deezer.com, использование технологии FLAC'
                    )
                elif event.from_chat:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        chat_id=event.chat_id,
                         message= 'я слушаю музыку с моего flow листа на deezer https://deezer.com, использование технологии FLAC'
                    )  

            elif text in sub_what_games and history[-1] in what_games:
                if event.from_user:
                    vk.messages.send( 
                        peer_id = event.peer_id,
                        random_id = get_random_id(),
                        user_id=event.user_id,
                        message="игра была сложная, но мне она этим  понравилась "
                )
                elif event.from_chat: 
                    vk.messages.send( 
                        peer_id = event.peer_id,
                        random_id = get_random_id(),
                        chat_id=event.chat_id,
                         message="игра была сложная, но мне она этим понравилась"
                    )
            elif text in sub_what_games and not history[-1] in what_games:
                if event.from_user:
                            vk.messages.send(
                                peer_id=event.peer_id,
                                random_id=get_random_id(),
                                user_id=event.user_id,
                                message="о чем идет речь?"
                            )
                elif event.from_chat:
                            vk.messages.send(
                                peer_id=event.peer_id,
                                random_id=get_random_id(),
                                chat_id=event.chat_id,
                                message="о чем идет речь?"
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
                            message='я уже говорил что я умею, я умею переводить текст и искать информацию из интернета, парсить цены на видео карты'
                        )
                        elif event.from_chat:
                            vk.messages.send(
                            peer_id=event.peer_id,
                            random_id=get_random_id(),
                            chat_id=event.chat_id,
                            message='я уже говорил что я умею, я умею переводить текст и искать информацию из интернета, парсить цены на видео карты'
                        )
            elif text in existance_question:
                
                if event.from_user:
                    vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        user_id=event.user_id,
                        message=existance_answers[random.randint(0, 1)]
                    )
                elif event.from_chat:
                        vk.messages.send(
                        peer_id=event.peer_id,
                        random_id=get_random_id(),
                        chat_id=event.chat_id,
                        message=existance_answers[random.randint(0, 1)]
                    )
            elif text in sub_existance_question and history[-1] in existance_question:
            
                        if event.from_user:
                            vk.messages.send(
                            peer_id=event.peer_id,
                            random_id=get_random_id(),
                            user_id=event.user_id,
                            message="я уже ответил на этот вопрос, я слушаю музыку и все"
                        )
                        elif event.from_chat:
                            vk.messages.send(
                            peer_id=event.peer_id,
                            random_id=get_random_id(),
                            chat_id=event.chat_id,
                            message="я уже ответил на этот вопрос, я слушаю музыку и все"
                        ) 
            elif text in sub_existance_question_dark and history[-1] in existance_question:
            
                        if event.from_user:
                            vk.messages.send(
                            peer_id=event.peer_id,
                            random_id=get_random_id(),
                            user_id=event.user_id,
                            message="не знаю почему все так грустно, лучше не быть совсем"
                        )
                        elif event.from_chat:
                            vk.messages.send(
                            peer_id=event.peer_id,
                            random_id=get_random_id(),
                            chat_id=event.chat_id,
                            message="не знаю почему все так грустно, лучше не быть совсем"
                        )                                    
            elif text.split(' ')[0] == "переведи" and text.split(' ')[2] == "русский":
                words = text.split(' ')
                del words[0]
                del words[0]
                del words[0]
                result = translate(words, 'ru')
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
            elif text.split(' ')[0] == "переведи" and text.split(' ')[2] == "французский":
                words = text.split(' ')
                del words[0]
                del words[0]
                del words[0]
                result = translate(words, 'fr')
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
            elif text.split(' ')[0] == "переведи" and text.split(' ')[2] == "немецкий":
                words = text.split(' ')
                del words[0]
                del words[0]
                del words[0]
                result = translate(words, 'de')
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

            else:
                word_list = text.split(' ')
                for i in word_list:
                    lang = 'en'
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