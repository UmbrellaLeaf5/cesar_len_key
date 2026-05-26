import pytest

from cesar_len_key.alphabet_shuffle import (
  DivisorsList,
  PiecewiseShuffledAlphabet,
  RemadeKey,
  ShuffledAlphabet,
)


class TestDivisorsList:
  """Тесты для функции DivisorsList."""

  def test_six_returns_four_divisors(self) -> None:
    """6 возвращает [1, 2, 3, 6]."""

    assert DivisorsList(6) == [1, 2, 3, 6]

  def test_prime_returns_two_divisors(self) -> None:
    """7 (простое) возвращает [1, 7]."""

    assert DivisorsList(7) == [1, 7]

  def test_one_returns_one_divisor(self) -> None:
    """1 возвращает [1]."""

    assert DivisorsList(1) == [1]

  def test_perfect_square_returns_odd_divisor_count(self) -> None:
    """16 (полный квадрат) возвращает [1, 2, 4, 8, 16]."""

    assert DivisorsList(16) == [1, 2, 4, 8, 16]

  def test_twelve_returns_all_divisors(self) -> None:
    """12 возвращает [1, 2, 3, 4, 6, 12]."""

    assert DivisorsList(12) == [1, 2, 3, 4, 6, 12]


class TestRemadeKey:
  """Тесты для функции RemadeKey."""

  def test_simple_key_no_duplicates(self) -> None:
    """Ключ 'key' без повторов преобразуется в числовой ключ."""

    assert RemadeKey("key", 100) == [1, 0, 2]

  def test_key_with_duplicate_chars_removes_duplicates(self) -> None:
    """'hello' → 'helo' → числовой ключ без дубликатов."""

    assert RemadeKey("hello", 100) == [1, 0, 2, 3]

  def test_key_with_spaces_removes_spaces(self) -> None:
    """Пробелы удаляются из ключа перед преобразованием."""

    # "c a b a" → после удаления пробелов и дубликатов → "cab"
    assert RemadeKey("c a b a", 100) == [2, 0, 1]

  def test_key_longer_than_max_len_truncated(self) -> None:
    """Ключ 'abcd' с max_len=2 обрезается до 'ab'."""

    assert RemadeKey("abcd", 2) == [0, 1]

  def test_key_only_spaces_raises_error(self) -> None:
    """Ключ, состоящий только из пробелов, вызывает ValueError."""

    with pytest.raises(ValueError, match="invalid key"):
      RemadeKey("   ", 100)

  def test_empty_key_raises_error(self) -> None:
    """Пустой ключ вызывает ValueError."""

    with pytest.raises(ValueError, match="invalid key"):
      RemadeKey("", 100)

  def test_key_max_len_equals_alphabet_length(self) -> None:
    """Ключ 'key' с max_len=3 не обрезается."""

    assert RemadeKey("key", 3) == [1, 0, 2]


class TestPiecewiseShuffledAlphabet:
  """Тесты для функции PiecewiseShuffledAlphabet."""

  def test_empty_alphabet_returns_empty_list(self) -> None:
    """Пустой алфавит возвращает пустой список."""

    assert PiecewiseShuffledAlphabet("key", "") == []

  def test_alphabet_with_duplicates_raises_error(self) -> None:
    """Алфавит с повторяющимися символами вызывает ValueError."""

    with pytest.raises(ValueError, match="invalid alphabet"):
      PiecewiseShuffledAlphabet("key", "aab")

  def test_single_char_in_alphabet(self) -> None:
    """Алфавит из одного символа остаётся без изменений."""

    assert PiecewiseShuffledAlphabet("x", "a") == ["a"]

  def test_key_divides_alphabet_evenly(self) -> None:
    """Алфавит делится на блоки по длине ключа, каждый блок перемешивается."""

    result = PiecewiseShuffledAlphabet("ba", "abcdef")
    assert result == ["ba", "dc", "fe"]

  def test_key_does_not_divide_alphabet_evenly(self) -> None:
    """Если длина алфавита не кратна длине ключа, ищется ближайший делитель."""

    original_length = 7
    result = PiecewiseShuffledAlphabet("ba", "abcdefg")
    assert len("".join(result)) == original_length
    # блоки перемешаны — порядок изменился относительно исходного
    assert result != ["a", "b", "c", "d", "e", "f", "g"]

  def test_two_char_alphabet(self) -> None:
    """Алфавит из двух символов с ключом из двух символов."""

    result = PiecewiseShuffledAlphabet("ba", "ab")
    assert len(result) == 1
    assert len(result[0]) == len("ab")
    assert result == ["ba"]

  def test_long_key_with_short_alphabet(self) -> None:
    """Ключ длиннее алфавита обрезается до длины алфавита."""

    alph = "abc"
    result = PiecewiseShuffledAlphabet("оченьдлинныйключ", alph)
    assert len("".join(result)) == len(alph)


class TestShuffledAlphabet:
  """Тесты для функции ShuffledAlphabet."""

  def test_returns_string(self) -> None:
    """Функция возвращает строку, а не список."""

    result = ShuffledAlphabet("test", "abcdefghij")
    assert isinstance(result, str)

  def test_deterministic(self) -> None:
    """Одинаковые входные данные дают одинаковый результат."""

    a = ShuffledAlphabet("secret", "abcdefghijklmnop")
    b = ShuffledAlphabet("secret", "abcdefghijklmnop")
    assert a == b

  def test_different_keys_different_result(self) -> None:
    """Разные ключи дают разные перемешанные алфавиты."""

    alph = "abcdefghijklmnopqrstuvwxyz"
    a = ShuffledAlphabet("abc", alph)
    b = ShuffledAlphabet("cba", alph)
    assert a != b

  def test_alphabet_length_preserved(self) -> None:
    """Перемешанный алфавит имеет ту же длину, что и исходный."""

    alph = "abcdefghijklmnopqrstuvwxyz"
    assert len(ShuffledAlphabet("key", alph)) == len(alph)

  def test_no_symbol_loss(self) -> None:
    """Все символы исходного алфавита присутствуют в перемешанном."""

    alph = "abcdefghijklmnop"
    result = ShuffledAlphabet("key", alph)
    assert sorted(result) == sorted(alph)

  def test_small_alphabet_less_than_three(self) -> None:
    """Алфавит из двух символов — краевой случай < 3."""

    alph = "ab"
    result = ShuffledAlphabet("k", alph)
    assert len(result) == len(alph)
    assert sorted(result) == sorted(alph)

  def test_key_longer_than_alphabet(self) -> None:
    """Ключ длиннее алфавита: ключ обрезается, алфавит перемешивается."""

    alph = "abcdef"
    result = ShuffledAlphabet("длинныйключ", alph)
    assert len(result) == len(alph)
    assert sorted(result) == sorted(alph)
