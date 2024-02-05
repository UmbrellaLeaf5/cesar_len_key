from utility import divisors_list
from alphabet_shuffle import shuffled_alphabet
from word_cryption import crypted_word, CryptType

# MEANS: алфавит, используемый во всей программе
alph = '!%()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^`abcdefghijklmnopqrstuvwxyz|~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё'

# MEANS: список делителей числа - длины алфавита
alph_divs = divisors_list(len(alph))

# MEANS: последний делитель из списка делителй длины алфавита
last_div = alph_divs[len(alph_divs) - 1]


def main():
    print('(REMEMBER that only characters of this sequence (and spaces) can be used in the text:')
    print()
    print(
        '!%()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^`abcdefghijklmnopqrs')
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
    flag: CryptType = CryptType.decr
    flack = ''
    while flack != '0':
        if flack == '1':
            flag = CryptType.encr
            break
        if flack != '':
            print('Enter 0 or 1.')
            print()
        print('Encryption (Enter 1) or Decryption (Enter 0)?')
        flack = input()
        if flack == 'Encryption' or flack == 'encryption':
            flag = CryptType.encr
        elif flack == 'Decryption' or flack == 'decryption':
            flag = CryptType.decr

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
    result: str = ''
    for i in range(len(listw) - 1):
        if listw[i] != ' ':
            result += crypted_word(listw[i], flag,
                                   shuffled_alphabet(kluch, alph))
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
