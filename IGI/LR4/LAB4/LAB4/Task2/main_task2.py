# -*- coding: cp1251 -*-

from Task2.functions_task2 import TextAnalyzer

def main_task2():
    print("Текст будет получаться из файла TestForTask2.txt")
    
    analyzer = TextAnalyzer("TestForTask2.txt")
    analysis_results = analyzer.analyze_text()
    
    analyzer.save_results_to_file("OutputForTask2.txt", analysis_results)
    analyzer.zip_results_file("OutputForTask2.txt", "OutputForTask2Zip.zip")
    
    analyzer.print_results(analysis_results)
    
    replacement_symbol = input("\nВведите символ для замены пробелов: ")
    modified_text = analyzer.replace_spaces(replacement_symbol)
    print("\nТекст с замененными пробелами:")
    print(modified_text)

    guid_with_brackets = "e02fd0e4-00fd-090A-ca30-0d00a0038ba0"
    guid_without_brackets = "e02fd0e400fd090Aca300d00a0038ba0"
    print(f"Строка {guid_with_brackets} {'со скобками' if analyzer.is_guid_with_brackets(guid_with_brackets) else 'без скобок'}")
    print(f"Строка {guid_without_brackets} {'со скобками' if analyzer.is_guid_with_brackets(guid_without_brackets) else 'без скобок'}")