morse_alphabet = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}
switched_morse_alphabet = {v: k for k, v in morse_alphabet.items()}

message = input().split(' | ')
encrypted_message = ''
for word in message:
    word_sep = word.split()
    for letter in word_sep:
        encrypted_message += switched_morse_alphabet[letter]
    encrypted_message += ' '
print(encrypted_message)
