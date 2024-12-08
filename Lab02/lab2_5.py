"""
Korzystając z przykładu przedstawionego na wykładzie, określ tekst jawny szyfrogramu zaszyfrowanego przy użyciu szyfru podstawieniowego. W rozwiązaniu opisz wykonane kroki obliczeniowe.

EMGLOSUDCGDNCUSWYSFHNSFCYKDPUMLWGYICOXYSIPJCK
QPKUGKMGOLICGINCGACKSNISACYKZSCKXECJCKSHYSXCG
OIDPKZCNKSHICGIWYGKKGKGOLDSILKGOIUSIGLEDSPWZU
GFZCCNDGYYSFUSZCNXEOJNCGYEOWEUPXEZGACGNFGLKNS
ACIGOIYCKXCJUCIUZCFZCCNDGYYSFEUEKUZCSOCFZCCNC
IACZEJNCSHFZEJZEGMXCYHCJUMGKUCY

Wskazówka: F odszyfrowuje się na w.
"""

import collections

def get_letter_frequency(text):
    frequency = collections.Counter(text)
    return frequency

def get_ngram_frequency(text, n):
    ngrams = [text[i:i+n] for i in range(len(text) - n + 1)]
    frequency = collections.Counter(ngrams)
    return frequency

def decrypt_with_mapping(ciphertext, mapping):
    decrypted_text = ''
    for char in ciphertext:
        if char in mapping:
            decrypted_text += mapping[char]
        else:
            decrypted_text += char
    return decrypted_text

def decrypt_caesar_shift(ciphertext, shift):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = "EMGLOSUDCGDNCUSWYSFHNSFCYKDPUMLWGYICOXYSIPJCKQPKUGKMGOLICGINCGACKSNISACYKZSCKXECJCKSHYSXCGOIDPKZCNKSHICGIWYGKKGKGOLDSILKGOIUSIGLEDSPWZUGFZCCNDGYYSFUSZCNXEOJNCGYEOWEUPXEZGACGNFGLKNSACIGOIYCKXCJUCIUZCFZCCNDGYYSFEUEKUZCSOCFZCCNCIACZEJNCSHFZEJZEGMXCYHCJUMGKUCY"
english_frequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

cipher_frequency = get_letter_frequency(ciphertext)

sorted_cipher_letters = [item[0] for item in cipher_frequency.most_common()]

mapping = {}
for i in range(len(sorted_cipher_letters)):
    mapping[sorted_cipher_letters[i]] = english_frequency[i]

mapping['F'] = 'W'
mapping['M'] = 'M'
mapping['E'] = 'I'
mapping['C'] = 'E'
mapping['U'] = 'T'
mapping['G'] = 'A'
mapping['S'] = 'O'
mapping['Z'] = 'H'
mapping['N'] = 'L'

mapping['O'] = 'N'
mapping['Y'] = 'R'
mapping['W'] = 'G'
mapping['D'] = 'B'

digram_frequency = get_ngram_frequency(ciphertext, 2)
trigram_frequency = get_ngram_frequency(ciphertext, 3)

print("Ciphertext:", ciphertext)
print("Letter frequency in ciphertext:", cipher_frequency)
print("\nDigram frequency:", digram_frequency.most_common(10))
print("\nTrigram frequency:", trigram_frequency.most_common(10))
print("Decryption mapping:", mapping)

decrypted_message = decrypt_with_mapping(ciphertext, mapping)
print("\nDecrypted message using frequency analysis:", decrypted_message.lower())

# Domyslanie sie:
# I may not be able to grow slower but my garden
# Trzeba zgadywac kolejne litery w trybie "educated guesses" dopasowujac kolejne litery