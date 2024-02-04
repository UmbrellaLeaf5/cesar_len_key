from utility import divisors_list


def remaked_key(key: str, max_len: int) -> str:
    """
    Меняет ключ так, чтобы его можно было использовать для перемешивания алфавита

    ARGS:
        key (str): ключ
        max_len (int): максимальная допустиамя длина для ключа

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
        # по убыванию ищем близжайший делитель к числу - длине ключа
        for i in range(len(alph_divs) - 1, 0, -1):
            if len(key) > alph_divs[i]:
                # при нахождении такового, берем предыдущий, чтобы не обрезать ключ
                needed_div = alph_divs[i + 1]
                break

    # MEANS: разделенный на кусочки длинной needed_div алфавит
    listed_alph = [alph[i: i + needed_div]
                   for i in range(0, len(alph), needed_div)]

    sort_key_list = []
    for i in range(len(key)):
        sort_key_list.append(i)
    first_key = []
    for i in range(len(key)):
        first_key.append(key[i])
    first_key = sorted(first_key)

    final_key = []
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i] == first_key[j]:
                final_key.append(sort_key_list[j])

    if len(key) != needed_div:
        x = 0
        for i in range(len(key), needed_div):
            final_key.append(len(key) + x)
            x += 1

    for i in range(len(listed_alph)):
        temp = ''
        for j in range(len(listed_alph[i])):
            temp += (listed_alph[i])[final_key[j]]
        listed_alph[i] = temp

    alph = ''
    for i in range(len(listed_alph)):
        alph += listed_alph[i]
    return alph
