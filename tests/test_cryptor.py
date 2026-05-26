from cryptor import DEFAULT_ALPHABET, crypt_lines, crypt_words
from word_cryption import CryptType


class TestCryptWords:
  """Тесты для функции crypt_words."""

  def test_encrypt_decrypt_roundtrip(self) -> None:
    """Слово, зашифрованное и затем расшифрованное, совпадает с исходным."""

    words = ["hello", "world", "test"]
    key = "secret"
    encrypted = crypt_words(words, key, DEFAULT_ALPHABET, CryptType.encr)
    decrypted = crypt_words(encrypted, key, DEFAULT_ALPHABET, CryptType.decr)
    assert decrypted == words

  def test_deterministic_encryption(self) -> None:
    """Одинаковые входные данные дают одинаковый шифротекст."""

    words = ["abc", "def"]
    key = "test"
    a = crypt_words(words, key, DEFAULT_ALPHABET, CryptType.encr)
    b = crypt_words(words, key, DEFAULT_ALPHABET, CryptType.encr)
    assert a == b

  def test_empty_list(self) -> None:
    """Пустой список возвращает пустой список."""

    assert crypt_words([], "key", DEFAULT_ALPHABET) == []

  def test_non_alphabet_chars_unchanged(self) -> None:
    """Символы вне алфавита остаются без изменений."""

    words = ["a@b", "c#d"]
    result = crypt_words(words, "key", "abcd", CryptType.encr)
    # @ и # не в алфавите, должны остаться
    assert "@" in result[0]
    assert "#" in result[1]

  def test_different_keys_different_result(self) -> None:
    """Разные ключи дают разный шифротекст."""

    words = ["hello"]
    a = crypt_words(words, "ab", DEFAULT_ALPHABET, CryptType.encr)
    b = crypt_words(words, "abcdefgh", DEFAULT_ALPHABET, CryptType.encr)
    assert a != b


class TestCryptLines:
  """Тесты для функции crypt_lines."""

  def test_roundtrip(self) -> None:
    """Строки, зашифрованные и расшифрованные, совпадают с исходными."""

    lines = ["hello world", "test line", ""]
    key = "secret"
    encrypted = crypt_lines(lines, key, DEFAULT_ALPHABET, CryptType.encr)
    decrypted = crypt_lines(encrypted, key, DEFAULT_ALPHABET, CryptType.decr)
    assert decrypted == lines

  def test_preserves_line_count(self) -> None:
    """Количество строк сохраняется после шифрования."""

    lines = ["first", "second", "third", ""]
    result = crypt_lines(lines, "key", DEFAULT_ALPHABET)
    assert len(result) == len(lines)

  def test_preserves_word_count_per_line(self) -> None:
    """Количество слов в каждой строке сохраняется."""

    lines = ["one two three", "four five", "six"]
    result = crypt_lines(lines, "key", DEFAULT_ALPHABET)
    for i, line in enumerate(lines):
      assert len(result[i].split()) == len(line.split())

  def test_empty_lines_preserved(self) -> None:
    """Пустые строки остаются пустыми."""

    lines = ["hello", "", "world", ""]
    result = crypt_lines(lines, "key", DEFAULT_ALPHABET)
    assert result[0] != ""
    assert result[1] == ""
    assert result[2] != ""
    assert result[3] == ""

  def test_empty_list(self) -> None:
    """Пустой список возвращает пустой список."""

    assert crypt_lines([], "key", DEFAULT_ALPHABET) == []
