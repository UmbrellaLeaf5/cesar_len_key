import os
import tempfile


class TestFileCryptCLI:
  """Интеграционные тесты для file_crypt.py CLI."""

  def test_encrypt_decrypt_file_roundtrip(self) -> None:
    """Файл, зашифрованный и расшифрованный, совпадает с исходным."""

    original_content = "hello world\ntest line\nanother line"

    with tempfile.TemporaryDirectory() as tmpdir:
      # Means: путь к временному файлу
      input_path = os.path.join(tmpdir, "input.txt")
      encrypted_path = os.path.join(tmpdir, "encrypted.txt")
      decrypted_path = os.path.join(tmpdir, "decrypted.txt")

      # создаём исходный файл
      with open(input_path, "w", encoding="utf-8") as f:
        f.write(original_content)

      # шифруем
      exit_code = os.system(
        f'python scripts/file_crypt.py "{input_path}" -k secret -o "{encrypted_path}"'
      )
      assert exit_code == 0

      # расшифровываем
      exit_code = os.system(
        f'python scripts/file_crypt.py "{encrypted_path}"'
        f' -k secret -d -o "{decrypted_path}"'
      )
      assert exit_code == 0

      # проверяем содержимое
      with open(decrypted_path, encoding="utf-8") as f:
        decrypted_content = f.read()

      assert decrypted_content == original_content

  def test_output_written_to_specified_path(self) -> None:
    """Выходной файл записывается в указанный путь -o."""

    original_content = "test content"

    with tempfile.TemporaryDirectory() as tmpdir:
      input_path = os.path.join(tmpdir, "input.txt")
      output_path = os.path.join(tmpdir, "custom_output.txt")

      with open(input_path, "w", encoding="utf-8") as f:
        f.write(original_content)

      exit_code = os.system(
        f'python scripts/file_crypt.py "{input_path}" -k key -o "{output_path}"'
      )
      assert exit_code == 0
      assert os.path.exists(output_path)

      with open(output_path, encoding="utf-8") as f:
        content = f.read()

      assert content != original_content

  def test_missing_key_shows_error(self) -> None:
    """Отсутствие ключа -k показывает ошибку и выходит."""

    with tempfile.TemporaryDirectory() as tmpdir:
      input_path = os.path.join(tmpdir, "input.txt")

      with open(input_path, "w", encoding="utf-8") as f:
        f.write("test")

      # ключ не указан — должно выйти с ошибкой
      exit_code = os.system(f'python scripts/file_crypt.py "{input_path}" 2>/dev/null')
      assert exit_code != 0

  def test_nonexistent_input_file_shows_error(self) -> None:
    """Несуществующий входной файл показывает ошибку."""

    # файл не существует
    exit_code = os.system(
      'python scripts/file_crypt.py "/nonexistent/path/file.txt" -k key 2>/dev/null'
    )
    assert exit_code != 0

  def test_empty_file_produces_empty_output(self) -> None:
    """Пустой файл производит пустой выход."""

    with tempfile.TemporaryDirectory() as tmpdir:
      input_path = os.path.join(tmpdir, "empty.txt")
      output_path = os.path.join(tmpdir, "output.txt")

      # создаём пустой файл
      with open(input_path, "w", encoding="utf-8") as f:
        pass

      exit_code = os.system(
        f'python scripts/file_crypt.py "{input_path}" -k key -o "{output_path}"'
      )
      assert exit_code == 0

      with open(output_path, encoding="utf-8") as f:
        content = f.read()

      assert content == ""
