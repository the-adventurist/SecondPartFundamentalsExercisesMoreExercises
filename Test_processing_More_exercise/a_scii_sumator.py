start_letter = input()
end_letter = input()
random_text = input()

sum_values = 0
for letter in random_text:
    if ord(start_letter) < ord(letter) < ord(end_letter):
        sum_values += ord(letter)
print(sum_values)
