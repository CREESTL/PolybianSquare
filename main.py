import random
import math


# Функция вывода полибианского квадрата на экран
def pretty_print(p_square):
    print("Полученный полибианский квадрат: ")
    for line in p_square:
        print(line)


# Функция формирования полибианского квадрата
def form_p_square(chars, columns, rows):
    # Создается пустой двумерный массив
    p_square = [["" for i in range(columns)] for j in range(rows)]
    for i, char in enumerate(chars):
        # Определяется номер строки и столбца, в которые должен быть помещен символ
        num_row = i // columns
        num_column = i % columns
        # Символ помещается в данную позицию
        p_square[num_row][num_column] = char
    return p_square


# Функция нахождения позиции символа в полибианском квадрате
def find_char(p_square, char):
    # Проверяется каждая строка
    for row_num, row in enumerate(p_square):
        # И каждый символ строки
        if char in row:
            return row_num, row.index(char)
    return -1


# Функция шифрования исходной строки
def encode(p_square, string):
    # Строку необходимо привести к нижнему регистру
    string = string.lower()
    rows = len(p_square)
    code_string = ""
    for raw_char in string:
        # Находится позиция каждого элемента строки в полибианском квадрате
        raw_char_pos = find_char(p_square, raw_char)
        # Если позиция не была корректно обнаружена, это означает, что пользователь ввел недопустимый символ
        if raw_char_pos == -1:
            raise Exception("Вы ввели символ, который невозможно закодировать!")
        raw_row, raw_column = raw_char_pos
        # Если строка, в которой был обнаружен исходный символ, является
        # последней - для шифрования берется символ из первой строки
        if raw_row + 1 > (rows - 1):
            code_row = 0
        # Иначе - для шифрования берется символ из следующей строки
        else:
            code_row = raw_row + 1
        # Столбец остается неизменным
        code_column = raw_column
        # Выбирается зашифрованный символ и добавляется в конец зашифрованной строки
        code_char = p_square[code_row][code_column]
        code_string += code_char
    return code_string


# Функция расшифрования зашифрованной строки
def decode(p_square, string):
    rows = len(p_square)
    raw_string = ""
    for code_char in string:
        # Находится позиция каждого элемента строки в полибианском квадрате
        code_char_pos = find_char(p_square, code_char)
        # Если позиция не была корректно обнаружена, это означает, что для шифрования использовался другой ключ
        if code_char_pos == -1:
            raise Exception("Шифрование производилось не по этому полибианскому квадрату!")
        code_row, code_column = code_char_pos
        # Если строка, в которой был обнаружен зашифрованный символ, является первой, то в качестве исходной
        # берется последняя строка
        if code_row == 0:
            raw_row = rows - 1
        # Иначе - в качестве исходной берется предыдущая строка
        else:
            raw_row = code_row - 1
        # Столбец остается неизменным
        raw_column = code_column
        # Выбирается расшифрованный символ и добавляется в конец исходной строки
        raw_char = p_square[raw_row][raw_column]
        raw_string += raw_char
    return raw_string


# Главная функция программы
def main():
    # В качестве допустимых для шифрования символов используются все строчные буквы русского алфавита и три спец.символа
    russian_alphabet = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
    special_symbols = ',. '
    chars = russian_alphabet + special_symbols
    chars = [char for char in chars]
    # Символы перемешиваются
    random.shuffle(chars)

    # При имеющимся фиксированном количестве столбцов, подсчитывается необходимое количество строк
    COLUMNS = 7
    ROWS = math.floor(len(chars) / COLUMNS)
    # Формируется полибианский квадрат
    p_square = form_p_square(chars, COLUMNS, ROWS)
    pretty_print(p_square)

    # Введенная пользователем строка преобразуется в строчные буквы
    raw_string = input("Введите строку для шифрования: ")

    # Шифрование строки
    code_string = encode(p_square, raw_string)
    print(f"Зашифрованная строка: {code_string}")

    # Расшифровывание строки
    decode_string = decode(p_square, code_string)
    print(f'Расшифрованная строка: {decode_string}')

    # Работа с двумя требуемыми строками
    print("\nДве проверочные строки: ")
    default_string_1 = "НГТУ им. Р.Е.Алексеева"
    code_string = encode(p_square, default_string_1)
    decode_string = decode(p_square, code_string)
    print(f"Зашифрованная строка '{default_string_1}': {code_string}")
    print(f"Расшифрованная строка '{default_string_1}': {decode_string}")

    default_string_2 = "Егоров Данила Андреевич"
    code_string = encode(p_square, default_string_2)
    decode_string = decode(p_square, code_string)
    print(f"Зашифрованная строка '{default_string_2}': {code_string}")
    print(f"Расшифрованная строка '{default_string_2}': {decode_string}")


if __name__ == "__main__":
    main()


