import pytest

from word_cryption import CryptedWord, CryptType


class TestCryptType:
  """Тесты для перечисления CryptType."""

  def test_encr_has_value_true(self) -> None:
    """encr соответствует True."""

    assert CryptType.encr.value is True

  def test_decr_has_value_false(self) -> None:
    """decr соответствует False."""

    assert CryptType.decr.value is False

  def test_encr_and_decr_are_different(self) -> None:
    """encr и decr — разные значения перечисления."""

    assert CryptType.encr != CryptType.decr


class TestCryptedWord:
  """Тесты для функции CryptedWord."""

  # общий алфавит для тестов
  ALPH = "abcdefghij"

  def test_encrypt_decrypt_roundtrip(self) -> None:
    """Слово, зашифрованное и затем расшифрованное, совпадает с исходным."""

    word = "cad"
    key = "secret"
    encrypted = CryptedWord(word, key, self.ALPH, CryptType.encr)
    decrypted = CryptedWord(encrypted, key, self.ALPH, CryptType.decr)
    assert decrypted == word

  def test_encryption_deterministic(self) -> None:
    """Одинаковые входные данные дают одинаковый шифротекст."""

    word = "hello"
    key = "test"
    a = CryptedWord(word, key, self.ALPH, CryptType.encr)
    b = CryptedWord(word, key, self.ALPH, CryptType.encr)
    assert a == b

  def test_decryption_deterministic(self) -> None:
    """Одинаковые входные данные дают одинаковый расшифрованный текст."""

    word = "encrypted"
    key = "test"
    a = CryptedWord(word, key, self.ALPH, CryptType.decr)
    b = CryptedWord(word, key, self.ALPH, CryptType.decr)
    assert a == b

  def test_non_alphabet_chars_unchanged(self) -> None:
    """Символы, которых нет в алфавите, остаются как есть."""

    key = "test"
    result = CryptedWord("a@b#c", key, self.ALPH, CryptType.encr)
    assert "@" in result
    assert "#" in result

  def test_empty_word_raises_zero_division(self) -> None:
    """Пустое слово приводит к ZeroDivisionError (известный баг)."""

    with pytest.raises(ZeroDivisionError):
      CryptedWord("", "key", self.ALPH, CryptType.encr)

  def test_different_keys_different_result(self) -> None:
    """Разные ключи дают разный шифротекст для одного слова."""

    word = "abcdef"
    a = CryptedWord(word, "аб", self.ALPH, CryptType.encr)
    b = CryptedWord(word, "abcdefgh", self.ALPH, CryptType.encr)
    assert a != b

  def test_different_words_different_result(self) -> None:
    """Разные слова дают разный шифротекст (при одном ключе)."""

    key = "test"
    a = CryptedWord("abc", key, self.ALPH, CryptType.encr)
    b = CryptedWord("abd", key, self.ALPH, CryptType.encr)
    assert a != b

  def test_word_length_preserved(self) -> None:
    """Длина зашифрованного слова равна длине исходного."""

    word = "abcdefghij"
    result = CryptedWord(word, "key", self.ALPH, CryptType.encr)
    assert len(result) == len(word)

  def test_decrypt_non_alphabet_chars(self) -> None:
    """При расшифровании неалфавитные символы проходят без изменений."""

    word = "a@b"
    encrypted = CryptedWord(word, "key", self.ALPH, CryptType.encr)
    decrypted = CryptedWord(encrypted, "key", self.ALPH, CryptType.decr)
    assert decrypted == word

  def test_single_char_roundtrip(self) -> None:
    """Слово из одного символа корректно шифруется и расшифровывается."""

    word = "a"
    key = "key"
    encrypted = CryptedWord(word, key, self.ALPH, CryptType.encr)
    decrypted = CryptedWord(encrypted, key, self.ALPH, CryptType.decr)
    assert decrypted == word

  def test_word_fully_outside_alphabet(self) -> None:
    """Слово, все символы которого вне алфавита, не изменяется."""

    word = "!!!"
    result = CryptedWord(word, "key", self.ALPH, CryptType.encr)
    assert result == word

  def test_long_alphabet_cyrillic(self) -> None:
    """Шифрование и расшифрование работают с большим алфавитом."""

    big_alph = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    word = "привет"
    key = "секрет"
    encrypted = CryptedWord(word, key, big_alph, CryptType.encr)
    decrypted = CryptedWord(encrypted, key, big_alph, CryptType.decr)
    assert decrypted == word
