def number_to_words(n):
    """Преобразует цифру в соответствующее слово на русском языке."""
    words = ["ноль", "один", "два", "три", "четыре", 
             "пять", "шесть", "семь", "восемь", "девять"]
    return words[n]

def process_lexemes(file_path):
    """
    Обрабатывает лексемы из файла:
    - Находит числа в двоичном формате
    - Проверяет, что число нечетное и <= 8192
    - Для подходящих чисел находит первую серию '11' и выводит:
      * Число без единиц
      * Позицию начала серии '11' (в словах)
    """
    with open(file_path, 'r') as file:
        data = file.read().split()
    
    for lexeme in data:
        # Пропускаем не двоичные числа
        if not all(c in '01' for c in lexeme):
            continue
            
        num = int(lexeme, 2)
        
        # Проверяем условия
        if num % 2 == 1 and num <= 8192:
            # Ищем серию '11'
            pos = lexeme.find('11')
            if pos != -1:  # Если серия найдена
                # Удаляем все единицы
                filtered = lexeme.replace('1', '')
                print(f"Число без единиц: {filtered}")
                
                # Нумерация позиций начинается с 1
                print(f"Позиция начала серии '11': {number_to_words(pos + 1)}")

# Пример использования
process_lexemes("input.txt")