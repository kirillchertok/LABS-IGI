# -*- coding: cp1251 -*-

from Task2.functions_task2 import TextAnalyzer

def main_task2():
    print("����� ����� ���������� �� ����� TestForTask2.txt")
    
    analyzer = TextAnalyzer("TestForTask2.txt")
    analysis_results = analyzer.analyze_text()
    
    analyzer.save_results_to_file("OutputForTask2.txt", analysis_results)
    analyzer.zip_results_file("OutputForTask2.txt", "OutputForTask2Zip.zip")
    
    analyzer.print_results(analysis_results)
    
    replacement_symbol = input("\n������� ������ ��� ������ ��������: ")
    modified_text = analyzer.replace_spaces(replacement_symbol)
    print("\n����� � ����������� ���������:")
    print(modified_text)

    guid_with_brackets = "e02fd0e4-00fd-090A-ca30-0d00a0038ba0"
    guid_without_brackets = "e02fd0e400fd090Aca300d00a0038ba0"
    print(f"������ {guid_with_brackets} {'�� ��������' if analyzer.is_guid_with_brackets(guid_with_brackets) else '��� ������'}")
    print(f"������ {guid_without_brackets} {'�� ��������' if analyzer.is_guid_with_brackets(guid_without_brackets) else '��� ������'}")