import requests #Обращаемся к библиотеке "requests"
r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# делаем запрос на сервер по переданному адресу
print(r.content) #Узнаем содержание
#############################

import requests
r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
print(r.status_code)  # узнаем статус полученного ответа
######################

import requests
r = requests.get('https://baconipsum.com/api/?type=meat-and-filler') #Через формат JSON
# попробуем поймать json ответ
print(r.content)
#####################

import requests
import json  # импортируем необходимую библиотеку
r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
print(type(texts))  # проверяем тип сконвертированных данных

for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
    print(text[:50], '\n')
 ###########################


import requests
import json

r = requests.get('https://api.github.com')
print(r.content) #Получим что-то типа словаря {} но это ещё не словарь
#####################################

import requests
import json

r = requests.get('https://api.github.com')

d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы

print(type(d))
print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений
#<class 'dict'>
#https://api.github.com/user/following{/target}
#######################################


#Отправимм теперь POST запрос
import requests
import json

data = {'key': 'value'}

r = requests.post('https://httpbin.org/post', json=json.dumps(
    data))  # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
print(r.content)
########################

#Создать программы отправляющую запрос на генерацию случайных текстов
#Испмользуем сервис по ссылке ниже
import requests
import json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')

r = json.loads(r.content)

print(r[0])