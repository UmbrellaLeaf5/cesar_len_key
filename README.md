# CesarLenKey

## About

A cryptographic program implementing an enhanced Caesar cipher algorithm with a dynamic key and non-linear transformations. The project combines classical approaches with modern mathematical methods to create robust encryption.

### Key features

- **Flexible shuffled alphabet** based on the user's key
- **Dynamic shift** using trigonometric functions
- **Multiple transformation layers** for increased cryptographic strength
- **Extended character support**: Latin, Cyrillic, special characters

### Mathematical foundation

#### 1. Shuffled alphabet generation

```python
def PiecewiseShuffledAlphabet(key: str, alph: str) -> list[str]:
```

- Computes divisors of the alphabet length for optimal partitioning
- Removes duplicates and spaces from the key
- Converts the key into a numeric sequence
- Splits the alphabet into blocks and shuffles each block by the key
- Merges blocks with additional permutation

#### 2. Dynamic shift calculation

```python
coef: float = abs(len(key) * sin(len(word) * len(key))) + len(key)
shift: int = abs(round(
    (coef ** 2)
    * (cos(len(word) / len(key) - 1) / sin(len(key) / len(word) + 1))
    * (sin(len(word) / len(key) + 1) / cos(len(key) / len(word) - 1))
))
```

Uses a non-linear combination of trigonometric functions of the key and text parameters, making the shift unpredictable.

#### 3. Additional transformations

- **Text reversal** under certain length conditions
- **Cyclic shift** of alphabet blocks
- **Modular arithmetic** for alphabet operations

### Technical details

- **Language**: Python 3.12
- **Encryption type**: Symmetric block encryption
- **Math foundation**: Trigonometric functions, modular arithmetic, number theory
- **Supported characters**: 150 symbols (Latin, Cyrillic, punctuation, special characters)

## Algorithm

### Step 1: Alphabet preparation

1. Input key is cleaned from duplicates and spaces
2. Optimal block sizes are calculated based on alphabet length divisors
3. Alphabet is split into blocks and shuffled by the key
4. Blocks are reordered to form the final alphabet

### Step 2: Encryption parameter calculation

1. A complexity coefficient is computed from key and text lengths
2. A dynamic shift is calculated using trigonometric functions
3. Additional text reversal is applied under specific conditions

### Step 3: Encryption / decryption

1. Each character is transformed through the shuffled alphabet
2. Dynamic shift is applied with modular arithmetic
3. Characters outside the alphabet are preserved unchanged

## Installation

### Requirements

- Python 3.12+
- Standard Python libraries: `math`, `enum`, `sys`

### Setup

```bash
git clone https://github.com/your-username/cesar_len_key.git
cd cesar_len_key
uv sync
```

### Running the interactive CLI

```bash
cesar-len-key
```

### Running the file encryption CLI

```bash
cesar-len-key-file input.txt -k mykey                    # encrypt
cesar-len-key-file input.txt -k mykey -d                 # decrypt
cesar-len-key-file input.txt -k mykey -o output.txt      # specify output
```

## Usage as a library in another project

Add the package as a git dependency via `uv`:

```bash
# In your other project:
uv add git+https://github.com/UmbrellaLeaf5/cesar_len_key
```

Then import and use the public API:

```python
from cesar_len_key import crypt_lines, crypt_words, CryptType, DEFAULT_ALPHABET

# Encrypt a flat list of words
words = ["password1", "secret_token"]
encrypted = crypt_words(words, "master_key")
decrypted = crypt_words(encrypted, "master_key", crypt_type=CryptType.decr)
assert decrypted == words

# Encrypt text line-by-line, preserving structure
lines = ["service: my_login", "password: my_password", ""]
encrypted_lines = crypt_lines(lines, "master_key")
decrypted_lines = crypt_lines(encrypted_lines, "master_key", crypt_type=CryptType.decr)
assert decrypted_lines == lines

# Use a custom alphabet (optional)
custom_alph = "abc123!@#"
result = crypt_words(["hello"], "key", alphabet=custom_alph)
```

### Public API

| Name               | Type     | Description                                    |
| ------------------ | -------- | ---------------------------------------------- |
| `crypt_lines`      | function | Encrypt/decrypt a list of strings line-by-line |
| `crypt_words`      | function | Encrypt/decrypt a flat list of words           |
| `CryptType`        | Enum     | `CryptType.encr` / `CryptType.decr`            |
| `CryptedWord`      | function | Low-level single-word encryption               |
| `DEFAULT_ALPHABET` | constant | The 150-character default alphabet             |

## Usage examples

### Interactive CLI (encryption)

```
WELCOME to the CesarLenKey! This is a program, where you can crypt your text!
       You can use Cyrillic or Latin alphabet and some specials chars.
                 (just try it, there is interesting algo :)

                       Enter text to crypt (1 string):
Hello, how is it going?

                Encryption (Enter 1) or Decryption (Enter 0)?
1

                      Enter cryption key (some string):
difiowefmjlkw2819

                    Result (with key difiowefmjlkw2819):
bJ)wt0 yt! 3X jc 3tVwL$

                 Press any key to continue using program...
                           (use Ctrl + Z to exit)

```

### Interactive CLI (decryption)

```
WELCOME to the CesarLenKey! This is a program, where you can crypt your text!
       You can use Cyrillic or Latin alphabet and some specials chars.
                 (just try it, there is interesting algo :)

                       Enter text to crypt (1 string):
bJ)wt0 yt! 3X jc 3tVwL$

                Encryption (Enter 1) or Decryption (Enter 0)?
0

                      Enter cryption key (some string):
difiowefmjlkw2819

                    Result (with key difiowefmjlkw2819):
Hello, how is it going?

                 Press any key to continue using program...
                           (use Ctrl + Z to exit)

```

## Key functions

- `DivisorsList()` — divisor computation for split optimization
- `RemadeKey()` — key to numeric sequence conversion
- `PiecewiseShuffledAlphabet()` — block-based alphabet shuffling
- `ShuffledAlphabet()` — final shuffled alphabet assembly
- `CryptedWord()` — core single-word encryption
- `crypt_words()` — public: encrypt/decrypt a word list
- `crypt_lines()` — public: encrypt/decrypt text line-by-line

## Future development

- [ ] Graphical interface (Tkinter/PyQt)
- [ ] Performance benchmarks and cryptanalysis
- [ ] Additional mathematical transformations
- [ ] Configurable alphabet modes

## Security notes

⚠️ **Important**: This algorithm is intended for educational and personal use. For protecting critically important information, use industry-standard encryption (AES, RSA, etc.).
