from enum import Enum
from math import cos, sin

from utility import switch


class CryptType(Enum):
    """
    MEANS
        тип операции: зашифровать или расшифровать

    Args:
        Enum (bool): тип операции
    """

    encr = True
    decr = False


def crypted_word(word: str, key: str, alph: str, crypt_type: CryptType) -> str:
    """
    Does:
        шифрует слово, используя сдвиг по алфавиту
        (вдохновлено шифром Цезаря)

    Args:
        word (str): исходной слово
        crypt_type (CryptType): шифрование/расшифрование
        alph (str): заданный алфавит

    Returns:
        str: шифрованное слово
    """

    # если длина алфавита делилась нацело на длину слова - разворачиваем
    # (сделано для большего усложнения алгоритма шифрования)
    if len(alph) % len(word) == 0:
        word = "".join(reversed(word))

    # Means: весёлый коэффициент
    coef = abs(len(key)*sin(len(word)*len(key))) + len(key)

    # Means: сдвиг по алфавиту (весёлая формула :)
    shift = abs(round((coef**2)*(cos(len(word)/len(key) - 1)/sin(len(key)/len(word) + 1))
                * (sin(len(word)/len(key) + 1)/cos(len(key)/len(word) - 1))))

    # Means: шифрованное слово
    crypted_word = ""

    # алгоритм самого Цезаря
    for char in word:
        if char in alph:
            # Means: индекс текущего элемента в этом алфавите
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
