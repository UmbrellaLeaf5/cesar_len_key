def d_list(x):
    dd = []
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            dd.append(i)
            if i != x//i:
                dd.append(x//i)
    return sorted(dd)


def rev_key(string, key):
    res = ''
    for i in range(len(string)):
        res += string[int(key[i])]

    res2 = []
    for i in range(len(string)):
        for j in range(len(string)):
            if string[i] == res[j]:
                res2.append(j)
    return res2


def kingdom(k, alph, sh):
    if len(k) != len(set(k)):
        for i in range(len(k)):
            if k[i] in k[0:i]:
                k = k[0:i] + ' ' + k[i + 1:len(k)]
    k = k.replace(' ', '')

    if len(k) > len(alph):
        key = k[0:len(alph)]
    else:
        key = k

    number2 = (d_list(len(alph)))[len((d_list(len(alph)))) - 1]
    for i in range(len(d_list(len(alph)))):
        if len(key) < (d_list(len(alph)))[i + int(i != len(d_list(len(alph))) - 1)]:
            number2 = (d_list(len(alph)))[i + int(len(alph) % len(key) != 0)]
            break

    listx = []
    for i in range(len(alph) // number2):
        listx.append(alph[0 + i * number2:number2 * (i + 1)])

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

    alph = ''
    for i in range(len(listx)):
        alph += listx[i]
    return alph


def sh_cesarlen(stri, shd, king):
    alph = '!%()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^abcdefghijklmnopqrstuvwxyz|~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё'
    alph = kingdom(king, alph, shd)

    if len(alph) % len(stri) == 0:
        stri = ''.join(reversed(stri))

    number1 = (d_list(len(alph)))[len((d_list(len(alph)))) - 1]
    for i in range(len(d_list(len(alph)))):
        if len(stri) < (d_list(len(alph)))[i + int(i != len(d_list(len(alph))) - 1)]:
            number1 = (d_list(len(alph)))[i + int(len(alph) % len(stri) != 0)]
            break

    listy = []
    for i in range(len(alph)//number1):
        listy.append(
            ''.join(reversed(alph[0 + i * number1:number1 * (i + 1)])))
    listy.append('')
    for i in range((len(listy) - 1)//2):
        if i % 2 != 0:
            listy[len(listy) - 1] = listy[i]
            listy[i] = listy[len(listy) - 1 - i]
            listy[len(listy) - 1 - i] = listy[len(listy) - 1]
    alph = ''
    for i in range(len(listy) - 1):
        alph += listy[i]

    stri2 = ''
    if shd == '1':
        for i in range(len(stri)):
            for j in range(len(alph)):
                if stri[i] == alph[j]:
                    if j + (len(stri) % len(alph)) < len(alph):
                        stri2 += alph[j + (len(stri) % len(alph))]
                    else:
                        stri2 += alph[j + (len(stri) % len(alph)) - len(alph)]
        return stri2
    if shd == '0':
        for i in range(len(stri)):
            for j in range(len(alph)):
                if stri[i] == alph[j]:
                    if j - (len(stri) % len(alph)) > 0:
                        stri2 += alph[j - (len(stri) % len(alph))]
                    elif (len(stri) % len(alph)) == j:
                        stri2 += alph[0]
                    else:
                        stri2 += alph[len(alph) - (len(stri) % len(alph)) + j]
        return stri2


seq = '!%()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^abcdefghijklmnopqrstuvwxyz|~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё'
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
        if not (string[i] in seq) and string[i] != ' ':
            string = string[0:i] + '0' + string[i + 1:len(string)]
    for i in range(2, len(string)):
        string = string.replace(' ' * i, ' ')
    string += ' '
    if string.replace(' ', '') == '':
        print('This does not work, the text must not consist of only spaces and must not be empty.')
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
