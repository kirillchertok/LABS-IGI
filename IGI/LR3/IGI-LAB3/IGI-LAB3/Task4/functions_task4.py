# -*- coding: cp1251 -*-

# Дата разработки : 29.03.2024
# Функции для 
# 1)Определения количества слов, состоящих из прописных букв
# 2)Поиска самого длинного слова начинающегося с 'l'
# 3)Поиска повторяющихся слов

# Функция для определения количества слов, состоящих из прописных букв
def find_words_upper(words):
    return sum(1 for word in words if word.isupper())

# Функция для поиска самого длинного слова начинающегося с 'l'
def find_largest_word_I(words):
    return max((word for word in words if(word.startswith('l'))),key=len, default=None)

# Функуия для поиска повторяющихся слов 
def find_repeat_words(words):
    repeated_words = set()
    unique_words = set()
    
    for word in words:
        if(word in unique_words):
            repeated_words.add(word)
        else:
            unique_words.add(word)
            
    return repeated_words        