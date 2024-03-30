# -*- coding: cp1251 -*-

# ������� ���������� �� ������ ��������� � ����/����� ������
# ���� ���������� : 29.03.2024

from Task4.functions_task4 import find_words_upper,find_largest_word_I,find_repeat_words

# �������� ������
text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."

# �������� �������
def main_task4():
    print("������� ��")
    print("1)����������� ���������� ����, ��������� �� ��������� ����")
    print("2)������ ������ �������� ����� ������������� � 'l'")
    print("3)������ ������������� ����\n")
    # ��������� ������ �� ����� 
    words = text.replace(',',' ').split()
    
    # ��������� ������ ������
    uppercase_word_count = find_words_upper(words)
    longest_I_word = find_largest_word_I(words)
    repeated_words = find_repeat_words(words)
    
    # ����� ���������� �����������
    print(f"���������� ����, ��������� �� ��������� ���� - {uppercase_word_count}")
    print(f"����� ������� ����� ������������ � 'I' - {longest_I_word}")
    print(f"������������� ����� - {repeated_words}")
