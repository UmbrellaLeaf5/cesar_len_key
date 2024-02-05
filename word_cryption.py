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


def crypted_word(word: str, shd: CryptType, key: str, alphabet: str) -> str:
    """
    DOES:
        шифрует слово, используя сдвиг по алфавиту
        (вдохновлено шифром Цезаря)

    ARGS:
        word (str): исходной слово
        shd (CryptType): шифрование/расшифрование
        alphabet (str): заданный алфавит

    RETURNS:
        str: за(рас)шифрованное слово
    """

    # если длина алфавита делилась нацело на длину слова - разворачиваем
    # (сделано для большего усложнения алгоритмма шифрования)
    if len(alphabet) % len(word) == 0:
        word = ''.join(reversed(word))

    w = len(word)
    k = len(key)
    # MEANS: сдвиг по алфавиту (весёлая формула)
    shift = abs(round(25*(cos(w/k - 1)/sin(k/w + 1))
                * (sin(w/k + 1)/cos(k/w - 1))))

    # MEANS: за(рас)шифрованное слово
    crypted_word = ""

    # алгоритм самого Цезаря
    for char in word:
        if char in alphabet:
            index = alphabet.index(char)
            # для простого выбора используем самописный switch-case
            for case in switch(shd):
                if case(CryptType.encr):
                    crypted_word += alphabet[(index + shift) % len(alphabet)]
                    break
                if case(CryptType.decr):
                    # в таком случае делаем обратный сдвиг
                    crypted_word += alphabet[(index - shift) % len(alphabet)]
                    break
        else:
            # (допускается случай, когда буквы нет в словаре)
            crypted_word += char

    return crypted_word
