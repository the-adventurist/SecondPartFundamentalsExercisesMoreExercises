word = input()
result_word = ''
for current_letter in range(len(word)):
    if current_letter == 0:
        result_word += word[current_letter]
    if result_word[-1] != word[current_letter]:
        result_word += word[current_letter]

print(result_word)
