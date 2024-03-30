# -*- coding: cp1251 -*-

# Функция отвечающая за начало программы и ввод/вывод данных
# Дата разработки : 29.03.2024

from Task4.functions_task4 import find_words_upper,find_largest_word_I,find_repeat_words

# Исходная строка
text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."

# Основная функция
def main_task4():
    print("Задание по")
    print("1)Определению количества слов, состоящих из прописных букв")
    print("2)Поиску самого длинного слова начинающегося с 'l'")
    print("3)Поиску повторяющихся слов\n")
    # Разделяем строку на слова 
    words = text.replace(',',' ').split()
    
    # Получение нужных данных
    uppercase_word_count = find_words_upper(words)
    longest_I_word = find_largest_word_I(words)
    repeated_words = find_repeat_words(words)
    
    # Вывод полученных результатов
    print(f"Количества слов, состоящих из прописных букв - {uppercase_word_count}")
    print(f"Самое длинное слово начинающееся с 'I' - {longest_I_word}")
    print(f"Повторяющиеся слова - {repeated_words}")
