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

    # MEANS: длина алфавита
    a_len = len(alph)

    # MEANS: список делителей числа - длины алфавита
    alph_divs = divisors_list(a_len)

    # MEANS: количество делителей числа - длины алфавита
    divs_amount = len(alph_divs)

    # MEANS: последний делитель из списка делителй числа - длины алфавита
    last_div = alph_divs[divs_amount - 1]

    # переделываем ключ
    key = remaked_key(key, a_len)

    print("len_key: ", len(key))
    for i in range(divs_amount):
        print("current div: ", alph_divs[i + int(i != divs_amount - 1)],
              len(key) < alph_divs[i + int(i != divs_amount - 1)])
        if len(key) < alph_divs[i + int(i != divs_amount - 1)]:
            last_div = alph_divs[i + int(a_len % len(key) != 0)]
            break
    print("last_div_value: ",
          alph_divs[i + int(a_len % len(key) != 0)])

    listx = []
    for i in range(a_len // last_div):
        listx.append(
            alph[0 + i * last_div:last_div * (i + 1)])

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

    if len(key) != last_div:
        x = 0
        for i in range(len(key), last_div):
            final_key.append(len(key) + x)
            x += 1

    for i in range(len(listx)):
        temp = ''
        for j in range(len(listx[i])):
            temp += (listx[i])[final_key[j]]
        listx[i] = temp

    alph = ''
    for i in range(len(listx)):
        alph += listx[i]
    return alph
