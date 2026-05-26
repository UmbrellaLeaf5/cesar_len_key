from alphabet_shuffle import ShuffledAlphabet
from word_cryption import CryptedWord, CryptType


# Means: алфавит по умолчанию, используемый во всей программе
DEFAULT_ALPHABET = (
  "!%()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^`abcdefghijklmnopqrs"
  + "tuvwxyz|~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё"
)


def crypt_words(
  words: list[str],
  key: str,
  alphabet: str = DEFAULT_ALPHABET,
  crypt_type: CryptType = CryptType.encr,
) -> list[str]:
  """
  Does:
      шифрует или расшифровывает список слов

  Args:
      words (list[str]): исходные слова
      key (str): ключ шифрования
      alphabet (str): алфавит
      crypt_type (CryptType): тип операции

  Returns:
      list[str]: список шифрованных слов
  """

  # Means: перемешанный алфавит
  shuffled = ShuffledAlphabet(key, alphabet)

  # Means: шифрованный текст
  return [CryptedWord(word, key, shuffled, crypt_type) for word in words]


def crypt_lines(
  lines: list[str],
  key: str,
  alphabet: str = DEFAULT_ALPHABET,
  crypt_type: CryptType = CryptType.encr,
) -> list[str]:
  """
  Does:
      шифрует или расшифровывает текст построчно, сохраняя разбивку на строки

  Args:
      lines (list[str]): исходные строки
      key (str): ключ шифрования
      alphabet (str): алфавит
      crypt_type (CryptType): тип операции

  Returns:
      list[str]: список шифрованных строк
  """

  # Means: перемешанный алфавит
  shuffled = ShuffledAlphabet(key, alphabet)

  # Means: шифрованные строки
  result: list[str] = []

  for line in lines:
    # Means: слова в строке
    words = line.split()

    # Means: шифрованные слова
    crypted = [CryptedWord(word, key, shuffled, crypt_type) for word in words]

    result.append(" ".join(crypted))

  return result
