from sys import exit

from utility import switch
from alphabet_shuffle import shuffled_alphabet
from word_cryption import crypted_word, CryptType


def welcome_message_print():
    """
    DOES:
        выводит приветственное сообщение пользователю

    """

    print("WELCOME to the CesarLenKey! This is a program, were you can crypt your text!")
    print('{:^76}'.format("(just try it, there are interesting algo :)"))
    print()


if __name__ == "__main__":
    welcome_message_print()

    while (True):
        # MEANS: алфавит, используемый во всей программе
        alph = '!%()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^`abcdefghijklmnopqrs\
                tuvwxyz|~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё'

        # ввод пользователем текста

        # MEANS: введенный пользователем текст
        text: list[str] = []

        while text == []:
            print('Enter text to crypt (1 string):')
            try:
                text = input().split()
            except EOFError or KeyboardInterrupt:
                exit()

        print()

        # ввод пользователем числа - типа операции

        # MEANS: тип операции
        crypt_type: CryptType = CryptType.decr

        # MEANS: введенное пользователем число
        input_number: int = -1

        print('Encryption (Enter 1) or Decryption (Enter 0)?')
        while input_number == -1:
            try:
                input_number = int(input())
                for case in switch(input_number):
                    if case(1):
                        crypt_type = CryptType.encr
                        break
                    if case(0):
                        crypt_type = CryptType.decr
                        break
                    if case():  # default
                        print("Enter 0 or 1")
                        input_number = -1
                        break

            except ValueError:
                print("Enter 0 or 1")

            except EOFError or KeyboardInterrupt:
                exit()

        print()

        # ввод пользователем ключа
        print('Enter key:')

        # MEANS: введенный пользователем ключ
        key: str

        try:
            key = input()

        except EOFError or KeyboardInterrupt:
            exit()

        # перемешивание алфавита
        alph = shuffled_alphabet(key, alph)

        # MEANS: за(рас)шифрованный текст
        crypted_text: list[str]

        # шифрование всего набора слов (введенного текста)
        crypted_text = [crypted_word(
            word, crypt_type, key, alph) for word in text]

        print()
        print('Result (with key ' + key + '):')
        print(' '.join(crypted_text))
        print()
        print('Press any key to continue...')
        input()
