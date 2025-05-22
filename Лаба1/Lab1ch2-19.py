import re

def number_to_words(n):
    """Преобразует число от 0 до 9 в соответствующее русское слово"""
    words = ["ноль", "один", "два", "три", "четыре",
             "пять", "шесть", "семь", "восемь", "девять"]
    return words[n]

def process_file(file_path):
    """
    Обрабатывает файл с двоичными числами, находя:
    1. Нечетные числа ≤ 8192
    2. Первую серию '11' в каждом таком числе
    3. Выводит число без единиц и позицию серии '11'
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            
            # Ищем все последовательности из 0 и 1 длиной ≥1
            binary_numbers = re.findall(r'\b[01]+\b', content)
            
            for binary in binary_numbers:
                num = int(binary, 2)
                
                # Проверяем условия: нечетное и ≤8192
                if num % 2 != 0 and num <= 8192:
                    # Ищем первую серию '11'
                    match = re.search(r'11', binary)
                    if match:
                        start_pos = match.start() + 1  # Позиция с 1
                        # Удаляем все единицы
                        without_ones = binary.replace('1', '')
                        
                        print(f"Двоичное число: {binary}")
                        print(f"Без единиц: {without_ones if without_ones else '0'}")
                        print(f"Позиция '11': {number_to_words(start_pos)}")
                        print("-" * 30)
    
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    input_file = "input.txt"
    process_file(input_file)