from utility import divisors_list


def remaked_key(key: str, max_len: int) -> list[int]:
    """
    Does: 
        преобразует ключ для использования в перемешивании алфавита

    Args:
        key (str): ключ
        max_len (int): максимальная допустимая длина для ключа

    Returns:
        str: ключ, содержащий в себе только числа, в порядке символов
    """

    # удаляем повторяющиеся символы, пробелы, сохраняя порядок
    if len(key) != len(set(key)):
        key = "".join(dict.fromkeys(key))
    key = key.replace(' ', "")

    # обрезаем, если ключ оказался длиннее алфавита
    if len(key) > max_len:
        key = key[0:max_len]

    # если после этих операций ключ оказался пустым, то он некорректен
    if (key == ""):
        raise ValueError("invalid key")

    # Means: последовательность чисел от 0 до длины ключа
    numbed_seq = list(range(len(key)))

    # Means: ключ, содержащий в себе только числа, в порядке символов
    numbed_key: list[int] = [
        numbed_seq[sorted(key).index(char)] for char in key]

    return numbed_key


def piecewise_shuffled_alphabet(key: str, alph: str) -> list[str]:
    """
    Does: 
        перемешивает куски алфавита, используя ключ

    Args:
        key (str): ключ
        alph (str): алфавит

    Returns:
        list[str]: кусочный алфавит, в котором каждая часть перемешана по ключу
    """

    # если в алфавите повторяются символы, то его нельзя брать за алфавит
    if (len(alph) != len(set(alph))):
        raise ValueError("invalid alphabet")

    # если алфавит ничего не содержит - с ним невозможно работать
    if (alph == ""):
        return list(alph)

    # Means: список делителей числа - длины алфавита
    alph_divs = divisors_list(len(alph))

    # Means: ключ, содержащий в себе только числа, в порядке символов
    numbed_key = remaked_key(key, len(alph))

    # Means: нужный делитель, по которому будет мешаться алфавит
    # (изначально равен последнему, чтобы обработать случай len(numbed_key) == len(alph))
    needed_div = alph_divs[len(alph_divs) - 1]

    # лучший случай: алфавит можно ровно поделить на длину ключа
    # (при этом ключ не равен по длине алфавиту)
    if (len(alph) % len(numbed_key) == 0 and len(alph) != len(numbed_key)):
        needed_div = len(numbed_key)

    else:
        # по убыванию ищем ближайший делитель к числу - длине ключа
        for i in range(len(alph_divs) - 1, 0, -1):
            if len(numbed_key) > alph_divs[i]:
                # при нахождении такового, берем предыдущий, чтобы не обрезать ключ
                # (берём i + 1 так как идём с конца)
                needed_div = alph_divs[i + 1]
                break
    # в цикле выше не нужно никаких рассмотрений доп. случаев,
    # так как они предусмотрены другими частями кода

    # Means: разделенный на кусочки длинной needed_div алфавит
    listed_alph = [alph[i: i + needed_div]
                   for i in range(0, len(alph), needed_div)]

    # если алфавит нельзя было ровно поделить на длину ключа, то ключ надо удлинить
    if len(numbed_key) != needed_div:
        numbed_key.extend(range(len(numbed_key), needed_div))

    # перемешиваем каждый элемент listed_alph в порядке numbed_key
    for i in range(len(listed_alph)):
        listed_alph[i] = "".join(listed_alph[i][numbed_key[j]]
                                 for j in range(len(listed_alph[i])))

    return listed_alph


def shuffled_alphabet(key: str, alph: str) -> str:
    """
    Does:
        перемешивает алфавит, используя ключ

    Args:
        key (str): ключ
        alph (str): алфавит

    Returns:
        str: перемешанный алфавит
    """

    # Means: кусочный алфавит, в котором каждая часть перемешана по ключу
    listed_alph = piecewise_shuffled_alphabet(key, alph)

    # Means: ключ, содержащий в себе только числа, в порядке символов
    numbed_key = remaked_key(key, len(alph))

    # если длина элемента кусочного словаря длинне ключа - дописываем его
    if len(listed_alph) > len(numbed_key):
        numbed_key.extend(range(len(numbed_key), len(listed_alph)))
    # иначе обрезаем
    elif len(listed_alph) < len(numbed_key):
        numbed_key = numbed_key[0:len(listed_alph)]

    # перемешиваем весь алфавит (куски как элементы) в соотв. с ключем
    shuffled_alph = [x for _, x in sorted(zip(numbed_key, listed_alph))]

    try:
        # возвращаем строку (ставя конечный элемент вначало)
        # (сделано для большего усложнения алгоритмма шифрования)
        return "".join(shuffled_alph[3::]) + "".join(shuffled_alph[0:3])
    except:
        # если элементов меньше 3, возвращаем, как есть
        return "".join(shuffled_alph)
