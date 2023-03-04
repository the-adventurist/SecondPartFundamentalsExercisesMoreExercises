first_word, second_word = input().split()

total_sum = 0

if len(first_word) < len(second_word):
    shorter_word = first_word
    longer_word = second_word
else:
    shorter_word = second_word
    longer_word = first_word

for current_symbol in range(len(shorter_word)):
    multiplication_result = ord(shorter_word[current_symbol]) * ord(longer_word[current_symbol])
    total_sum += multiplication_result

for current_symbol in range(len(shorter_word), len(longer_word)):
    total_sum += ord(longer_word[current_symbol])

print(total_sum)
