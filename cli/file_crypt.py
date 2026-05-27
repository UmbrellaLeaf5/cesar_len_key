import argparse
import sys

from cesar_len_key import DEFAULT_ALPHABET, CryptedLines, CryptType


def Main() -> None:
  """
  Does:
      точка входа для CLI-инструмента шифрования файлов
  """

  # Means: парсер аргументов командной строки
  parser = argparse.ArgumentParser(
    description="Шифрование и расшифрование файлов с помощью CesarLenKey"
  )

  parser.add_argument("input", help="путь к входному файлу")

  parser.add_argument("-k", "--key", required=True, help="ключ шифрования")

  parser.add_argument(
    "-o", "--output", help="путь к выходному файлу (по умолчанию перезаписывает входной)"
  )

  parser.add_argument(
    "-d",
    "--decrypt",
    action="store_true",
    help="режим расшифрования (по умолчанию шифрование)",
  )

  parser.add_argument(
    "-a", "--alphabet", default=DEFAULT_ALPHABET, help="алфавит для шифрования"
  )

  # Means: разобранные аргументы
  args = parser.parse_args()

  # Means: тип операции
  crypt_type = CryptType.decr if args.decrypt else CryptType.encr

  # чтение входного файла
  try:
    with open(args.input, encoding="utf-8") as f:
      # Means: строки файла
      lines = f.read().split("\n")

  except FileNotFoundError:
    print(f"Error: file '{args.input}' not found")
    sys.exit(1)

  except OSError as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

  # шифрование строк
  result = CryptedLines(lines, args.key, args.alphabet, crypt_type)

  # определение выходного пути
  output_path = args.output if args.output else args.input

  # запись выходного файла
  try:
    with open(output_path, "w", encoding="utf-8") as f:
      f.write("\n".join(result))

  except OSError as e:
    print(f"Error writing file: {e}")
    sys.exit(1)

  print(f"Done: {output_path}")


if __name__ == "__main__":
  Main()
