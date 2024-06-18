'''
Функции которые оставит в тексте только кириллические символы и пробелы. На вход она принимает текст, а возвращает очищенный текст.
'''
import pandas as pd
from pymystem3 import Mystem
import re

data = pd.read_csv('/datasets/tweets.csv')
corpus = list(data['text'])


def lemmatize(text):
    m = Mystem()
    lemm_list = m.lemmatize(text)
    lemm_text = "".join(lemm_list)    
    return lemm_text


def clear_text(text):
    return " ".join(re.sub(r'[^а-яА-ЯёЁ ]', ' ', text).split() ) 

print("Исходный текст:", corpus[0])
print("Очищенный и лемматизированный текст:", lemmatize(clear_text(corpus[0])))


# Результат работы кода
'''
Installing mystem to /home/student/.local/bin/mystem from http://download.cdn.yandex.net/mystem/mystem-3.1-linux-64bit.tar.gz
Исходный текст: @first_timee хоть я и школота, но поверь, у нас то же самое :D общество профилирующий предмет типа)
Очищенный и лемматизированный текст: хоть я и школоть но поверять у мы то же самый общество профилировать предмет тип
'''
