alph = '!%()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^abcdefghijklmnopqrstuvwxyz|~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё'


def divisors_list(x):
    # создание списка делителей перебором до корня
    listy = [i for i in range(1, int(x ** 0.5) + 1) if x % i == 0]

    # добавляем делители x // i (кроме случая, когда i равно x // i) в обратном порядке
    listy += [x // i for i in reversed(listy) if i != x // i]

    # возвращаем этот список отсортированным
    return sorted(listy)


def kingdom(k, alphabet):
    alph_len = len(alphabet)

    if len(k) != len(set(k)):
        for i in range(len(k)):
            if k[i] in k[0:i]:
                k = k[0:i] + ' ' + k[i + 1:len(k)]
    k = k.replace(' ', '')

    if len(k) > alph_len:
        key = k[0:alph_len]
    else:
        key = k

    number2 = (divisors_list(alph_len))[len((divisors_list(alph_len))) - 1]
    for i in range(len(divisors_list(alph_len))):
        if len(key) < (divisors_list(alph_len))[i + int(i != len(divisors_list(alph_len)) - 1)]:
            number2 = (divisors_list(alph_len))[
                i + int(alph_len % len(key) != 0)]
            break

    listx = []
    for i in range(alph_len // number2):
        listx.append(alphabet[0 + i * number2:number2 * (i + 1)])

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

    if len(key) != number2:
        x = 0
        for i in range(len(key), number2):
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
    new_alph = kingdom(king, alph)

    alph_len = len(alph)
    input_len = len(stri)

    if alph_len % input_len == 0:
        stri = ''.join(reversed(stri))

    last_alph_len_divisor = (divisors_list(alph_len))[
        len((divisors_list(alph_len))) - 1]
    for i in range(len(divisors_list(alph_len))):
        if input_len < (divisors_list(alph_len))[i + int(i != len(divisors_list(alph_len)) - 1)]:
            last_alph_len_divisor = (divisors_list(alph_len))[
                i + int(alph_len % input_len != 0)]
            break

    listy = []
    for i in range(alph_len//last_alph_len_divisor):
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
            for j in range(alph_len):
                if stri[i] == new_alph[j]:
                    if j + (input_len % alph_len) < alph_len:
                        stri2 += new_alph[j + (input_len % alph_len)]
                    else:
                        stri2 += new_alph[j +
                                          (input_len % alph_len) - alph_len]
        return stri2
    if shd == '0':
        for i in range(input_len):
            for j in range(alph_len):
                if stri[i] == new_alph[j]:
                    if j - (input_len % alph_len) > 0:
                        stri2 += new_alph[j - (input_len % alph_len)]
                    elif (input_len % alph_len) == j:
                        stri2 += new_alph[0]
                    else:
                        stri2 += new_alph[alph_len -
                                          (input_len % alph_len) + j]
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
