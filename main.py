from utility import divisors_list

# MEANS: алфавит, используемый во всей программе
alph = '!%()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^abcdefghijklmnopqrstuvwxyz|~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё'

# MEANS: длина алфавита, используемого во всей программе
a_len = len(alph)


def shuffled_alphabet(key: str, alphabet: str) -> str:
    """
    Перемешивает куски алфавита, используя длину ключа

    ARGS:
        key (str): ключ
        alphabet (str): алфавит

    RETURNS:
        str: перемешанный алфавит
    """

    # MEANS: длина алфавита
    alph_len = len(alphabet)

    # удаляем повторяющиеся символы, сохраняя порядок
    if len(key) != len(set(key)):
        key = ''.join(dict.fromkeys(key))

    # удаляем пробелы
    key = key.replace(' ', '')

    # обрезаем, если ключ оказался длиннее алфавита
    if len(key) > alph_len:
        key = key[0:alph_len]

    # MEANS: список делителей числа - длины алфавита
    alph_d_list = divisors_list(alph_len)

    # MEANS: последний делитель числа - длины алфавита
    last_alph_len_divisor = (alph_d_list)[
        len((alph_d_list)) - 1]

    for i in range(len(alph_d_list)):
        if len(key) < (alph_d_list)[i + int(i != len(alph_d_list) - 1)]:
            last_alph_len_divisor = (alph_d_list)[
                i + int(alph_len % len(key) != 0)]
            break

    listx = []
    for i in range(alph_len // last_alph_len_divisor):
        listx.append(
            alphabet[0 + i * last_alph_len_divisor:last_alph_len_divisor * (i + 1)])

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

    if len(key) != last_alph_len_divisor:
        x = 0
        for i in range(len(key), last_alph_len_divisor):
            final_key.append(len(key) + x)
            x += 1

    for i in range(len(listx)):
        temp = ''
        for j in range(len(listx[i])):
            temp += (listx[i])[final_key[j]]
        listx[i] = temp

    alphabet = ''
    for i in range(len(listx)):
        alphabet += listx[i]
    return alphabet


def sh_cesarlen(stri, shd, king):
    new_alph = shuffled_alphabet(king, alph)

    input_len = len(stri)

    if a_len % input_len == 0:
        stri = ''.join(reversed(stri))

    # MEANS: список делителей числа - длины алфавита
    alph_d_list = divisors_list(a_len)

    last_alph_len_divisor = (alph_d_list)[
        len((alph_d_list)) - 1]
    for i in range(len(alph_d_list)):
        if input_len < (alph_d_list)[i + int(i != len(alph_d_list) - 1)]:
            last_alph_len_divisor = (alph_d_list)[
                i + int(a_len % input_len != 0)]
            break

    listy = []
    for i in range(a_len//last_alph_len_divisor):
        listy.append(
            ''.join(reversed(new_alph[0 + i * last_alph_len_divisor:last_alph_len_divisor * (i + 1)])))
    listy.append('')
    for i in range((len(listy) - 1)//2):
        if i % 2 != 0:
            listy[len(listy) - 1] = listy[i]
            listy[i] = listy[len(listy) - 1 - i]
            listy[len(listy) - 1 - i] = listy[len(listy) - 1]
    new_alph = ''
    for i in range(len(listy) - 1):
        new_alph += listy[i]

    stri2 = ''
    if shd == '1':
        for i in range(input_len):
            for j in range(a_len):
                if stri[i] == new_alph[j]:
                    if j + (input_len % a_len) < a_len:
                        stri2 += new_alph[j + (input_len % a_len)]
                    else:
                        stri2 += new_alph[j +
                                          (input_len % a_len) - a_len]
        return stri2
    if shd == '0':
        for i in range(input_len):
            for j in range(a_len):
                if stri[i] == new_alph[j]:
                    if j - (input_len % a_len) > 0:
                        stri2 += new_alph[j - (input_len % a_len)]
                    elif (input_len % a_len) == j:
                        stri2 += new_alph[0]
                    else:
                        stri2 += new_alph[a_len -
                                          (input_len % a_len) + j]
        return stri2


def main():
    print('(REMEMBER that only characters of this sequence (and spaces) can be used in the text:')
    print()
    print(
        '!%()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^abcdefghijklmnopqrs')
    print('tuvwxyz|~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё')
    print()
    print('ALSO REMEMBER that the key should only consist of non-repeating characters)')
    print('(FAILURE TO FOLLOW the instructions above leads to incorrect operation of the program)')
    print()

    string = ''

    felper = True
    while felper:
        print('Enter text to crypt:')
        string = input()
        if string == '':
            string += ' '
        if string[0] == ' ':
            string = string[1:]
        for i in range(len(string)):
            if not (string[i] in alph) and string[i] != ' ':
                string = string[0:i] + '0' + string[i + 1:len(string)]
        for i in range(2, len(string)):
            string = string.replace(' ' * i, ' ')
        string += ' '
        if string.replace(' ', '') == '':
            print(
                'This does not work, the text must not consist of only spaces and must not be empty.')
            print()
        else:
            felper = False

    print()
    flack = ''
    while flack != '0':
        if flack == '1':
            break
        if flack != '':
            print('Enter 0 or 1.')
            print()
        print('Encryption (Enter 1) or Decryption (Enter 0)?')
        flack = input()
        if flack == 'Encryption' or flack == 'encryption':
            flack = '1'
        elif flack == 'Decryption' or flack == 'decryption':
            flack = '0'

    print()
    print('Enter key:')
    kluch = input()

    listw = []
    j = 0
    x = 0
    io = ''
    for i in string:
        if i == ' ' and io != i:
            listw.append(string[j:x])
            listw.append(' ')
            j = x + 1
        x += 1
        io = i
    listw[len(listw) - 1] = (listw[len(listw) - 1])[0:-1]
    result = ''
    for i in range(len(listw) - 1):
        if listw[i] != ' ':
            result += sh_cesarlen(listw[i], flack, kluch)
        else:
            result += listw[i]

    print()
    print('Result (with key ' + kluch + '):')
    print(result)
    print()
    print('Press any key to end...')
    input()


if __name__ == "__main__":
    main()
