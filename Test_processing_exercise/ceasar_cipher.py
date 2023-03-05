encrypted_version = input()
decrypted_version = ''

for symbol in encrypted_version:
    decrypted_version += chr(ord(symbol) + 3)

print(decrypted_version)
