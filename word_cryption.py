from enum import Enum
from math import cos, sin

from utility import switch


class CryptType(Enum):
    """
    MEANS
        тип операции: зашифровать или расшифровать

    ARGS:
        Enum (bool): тип операции
    """

    encr = True
    decr = False


def crypted_word(word: str, key: str, alph: str, crypt_type: CryptType) -> str:
    """
    DOES:
        шифрует слово, используя сдвиг по алфавиту
        (вдохновлено шифром Цезаря)

    ARGS:
        word (str): исходной слово
        crypt_type (CryptType): шифрование/расшифрование
        alph (str): заданный алфавит

    RETURNS:
        str: шифрованное слово
    """

    # если длина алфавита делилась нацело на длину слова - разворачиваем
    # (сделано для большего усложнения алгоритмма шифрования)
    if len(alph) % len(word) == 0:
        word = "".join(reversed(word))

    # MEANS: весёлый коэффициент
    koef = abs(len(key)*sin(len(word)*len(key))) + len(key)

    # MEANS: сдвиг по алфавиту (весёлая формула :)
    shift = abs(round((koef**2)*(cos(len(word)/len(key) - 1)/sin(len(key)/len(word) + 1))
                * (sin(len(word)/len(key) + 1)/cos(len(key)/len(word) - 1))))

    # MEANS: шифрованное слово
    crypted_word = ""

    # алгоритм самого Цезаря
    for char in word:
        if char in alph:
            # MEANS: индекс текущего элемента в этом алфавите
            index = alph.index(char)

            # для простого выбора используем самописный switch-case
            for case in switch(crypt_type):
                if case(CryptType.encr):
                    crypted_word += alph[(index + shift) % len(alph)]
                    break

                if case(CryptType.decr):
                    # в таком случае делаем обратный сдвиг
                    crypted_word += alph[(index - shift) % len(alph)]
                    break
        else:
            # (допускается случай, когда буквы нет в алфавите)
            crypted_word += char

    return crypted_word
