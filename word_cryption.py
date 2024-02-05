from enum import Enum


class CryptType(Enum):
    """
    Тип операции: зашифровать или расшифровать

    ARGS:
        Enum (_type_): тип операции
    """

    encr = True
    decr = False


def crypted_word(word: str, shd: CryptType, alphabet: str) -> str:
    """
    Шифрует слово по шифру цезаря, используя сдвиг на длину слова по заданному алфавиту

    ARGS:
        word (str): исходной слово
        shd (int): шифрование/расшифрование
        alphabet (str): заданный алфавит

    RETURNS:
        str: за(рас)шифрованное слово
    """

    # если длина алфавита делилась нацело на длину слова - разворачиваем
    # (сделано для большего усложнения алгоритмма шифрования)
    if len(alphabet) % len(word) == 0:
        word = ''.join(reversed(word))

    stri2 = ''
    if shd == CryptType.encr:
        for i in range(len(word)):
            for j in range(len(alphabet)):
                if word[i] == alphabet[j]:
                    if j + (len(word) % len(alphabet)) < len(alphabet):
                        stri2 += alphabet[j + (len(word) % len(alphabet))]
                    else:
                        stri2 += alphabet[j +
                                          (len(word) % len(alphabet)) - len(alphabet)]

    if shd == CryptType.decr:
        for i in range(len(word)):
            for j in range(len(alphabet)):
                if word[i] == alphabet[j]:
                    if j - (len(word) % len(alphabet)) > 0:
                        stri2 += alphabet[j - (len(word) % len(alphabet))]
                    elif (len(word) % len(alphabet)) == j:
                        stri2 += alphabet[0]
                    else:
                        stri2 += alphabet[len(alphabet) -
                                          (len(word) % len(alphabet)) + j]
    return stri2
