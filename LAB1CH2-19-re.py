import re

def number_to_words(n):
    digit_words = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }
    return ' '.join(digit_words[d] for d in str(n))

def is_valid_binary(binary_str):
    # Проверяем, что число:
    # 1) Содержит "11"
    # 2) Оканчивается на 1 (нечётное)
    # 3) Не превышает 8191 (1111111111111 в двоичной системе)
    pattern = r'^(?!.*1111111111111[01]*$)[01]*11[01]*1$'
    return re.fullmatch(pattern, binary_str) is not None

def process_lexemes(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            # Ищем все двоичные числа, удовлетворяющие условиям
            lexemes = re.findall(r'\b[01]+\b', data)
            
            for lexeme in lexemes:
                if is_valid_binary(lexeme):
                    # Удаляем все единицы
                    filtered_digits = re.sub(r'1', '', lexeme)
                    print(f"Число: {lexeme} -> Цифры без единиц: {filtered_digits}")
                    # Находим позицию первой "11"
                    match = re.search(r'11', lexeme)
                    if match:
                        pos = match.start() + 1
                        print(f"Позиция серии '11': {number_to_words(pos)}")
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")

process_lexemes("input.txt")