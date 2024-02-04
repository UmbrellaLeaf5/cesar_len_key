from utility import divisors_list


def remaked_key(key: str, max_len: int) -> str:
    """
    Меняет ключ так, чтобы его можно было использовать для перемешивания алфавита

    ARGS:
        key (str): ключ
        max_len (int): максимальная допустимая длина для ключа

    RETURNS:
        str: измененный ключ
    """

    # удаляем повторяющиеся символы, сохраняя порядок
    if len(key) != len(set(key)):
        key = ''.join(dict.fromkeys(key))

    # удаляем пробелы
    key = key.replace(' ', '')

    # обрезаем, если ключ оказался длиннее алфавита
    if len(key) > max_len:
        key = key[0:max_len]

    # если после этих операций ключ оказался пустым, то он некорректен
    if (key == ''):
        raise (ValueError("invalid key"))

    return key


def shuffled_alphabet(key: str, alph: str) -> str:
    """
    Перемешивает куски алфавита, используя ключ

    ARGS:
        key (str): ключ
        alph (str): алфавит

    RETURNS:
        str: перемешанный алфавит
    """

    # если алфавит ничего не содержит - с ним невозможно работать
    if (alph == ''):
        return alph

    # MEANS: список делителей числа - длины алфавита
    alph_divs = divisors_list(len(alph))

    # переделываем ключ
    key = remaked_key(key, len(alph))

    # MEANS: нужный делитель, по которому будет мешаться алфавит
    # (изначально равен последнему, чтобы обработать случай len(key) == len(alph))
    needed_div = alph_divs[len(alph_divs) - 1]

    # лучший случай: алфавит можно ровно поделить на длину ключа
    # (при этом ключ не равен по длине алфавиту)
    if (len(alph) % len(key) == 0 and len(alph) != len(key)):
        needed_div = len(key)

    else:
        # по убыванию ищем ближайший делитель к числу - длине ключа
        for i in range(len(alph_divs) - 1, 0, -1):
            if len(key) > alph_divs[i]:
                # при нахождении такового, берем предыдущий, чтобы не обрезать ключ
                needed_div = alph_divs[i + 1]
                break
    # в цикле выше не нужно никаких рассмотрений доп. случаев,
    # так как они предусмотрены другими частями кода

    # MEANS: разделенный на кусочки длинной needed_div алфавит
    listed_alph = [alph[i: i + needed_div]
                   for i in range(0, len(alph), needed_div)]

    # MEANS: последовательность чисел от 0 до длины ключа
    numbed_seq = list(range(len(key)))

    # MEANS: ключ, содержащий в себе только числа, в порядке символов
    numbed_key: list = [numbed_seq[sorted(key).index(char)] for char in key]

    # если алфавит нельзя было ровно поделить на длину ключа, то ключ надо удлинить
    if len(key) != needed_div:
        numbed_key.extend(range(len(key), needed_div))

    # перемешиваем каждый элемент listed_alph в порядке numbed_key
    for i in range(len(listed_alph)):
        listed_alph[i] = "".join(listed_alph[i][numbed_key[j]]
                                 for j in range(len(listed_alph[i])))

    return ''.join(listed_alph)
