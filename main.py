from sys import exit

from utility import switch
from alphabet_shuffle import shuffled_alphabet
from word_cryption import crypted_word, CryptType


def welcome_message_print():
    """
    DOES:
        выводит приветственное сообщение пользователю
    """

    print()

    print("WELCOME to the CesarLenKey! This is a program, where you can crypt your text!")
    print('{:^77}'.format(
        "You can use Cyrillic or Latin alphabet and some specials chars."))
    print('{:^77}'.format("(just try it, there are interesting algo :)"))

    print()


def next_usage_message_print():
    """
    DOES:
        выводит сообщение пользователю после очередного шифрования текста
    """
    print()

    print('{:^77}'.format('Press any key to continue using program...'))
    print('{:^77}'.format('(use Ctrl + Z to exit)'))

    print()


if __name__ == "__main__":
    welcome_message_print()

    while (True):
        # MEANS: алфавит, используемый во всей программе
        alph = "!%()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^`abcdefghijklmnopqrs" \
            + "tuvwxyz|~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё"

        # ввод пользователем текста

        # MEANS: введенный пользователем текст
        text: list[str] = []

        while text == []:
            print('{:^77}'.format('Enter text to crypt (1 string):'))
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

        print('{:^77}'.format('Encryption (Enter 1) or Decryption (Enter 0)?'))
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
        print('{:^77}'.format('Enter cryption key (some string):'))

        # MEANS: введенный пользователем ключ
        key: str = ""

        try:
            while key == "":
                key = input().replace(' ', "")

        except EOFError or KeyboardInterrupt:
            exit()

        # перемешивание алфавита
        try:
            alph = shuffled_alphabet(key, alph)

        except ValueError:
            # (учитывая, что алфавит здесь фиксирован, недостижимо)
            print("You're using wrong alphabet")
            exit()

        # MEANS: шифрованный текст
        crypted_text: list[str]

        # шифрование всего набора слов (введенного текста)
        crypted_text = [crypted_word(
            word, key, alph, crypt_type) for word in text]

        print()

        print('{:^77}'.format('Result (with key ' + key + '):'))
        print(' '.join(crypted_text))

        next_usage_message_print()

        try:
            input()

        except EOFError or KeyboardInterrupt:
            exit()
