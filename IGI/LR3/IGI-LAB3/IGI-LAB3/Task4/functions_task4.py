# -*- coding: cp1251 -*-

# ���� ���������� : 29.03.2024
# ������� ��� 
# 1)����������� ���������� ����, ��������� �� ��������� ����
# 2)������ ������ �������� ����� ������������� � 'l'
# 3)������ ������������� ����

# ������� ��� ����������� ���������� ����, ��������� �� ��������� ����
def find_words_upper(words):
    return sum(1 for word in words if word.isupper())

# ������� ��� ������ ������ �������� ����� ������������� � 'l'
def find_largest_word_I(words):
    return max((word for word in words if(word.startswith('l'))),key=len, default=None)

# ������� ��� ������ ������������� ���� 
def find_repeat_words(words):
    repeated_words = set()
    unique_words = set()
    
    for word in words:
        if(word in unique_words):
            repeated_words.add(word)
        else:
            unique_words.add(word)
            
    return repeated_words        