number_in_decimal = int(input())
state_of_binary = input()
number_as_binary = ''

while number_in_decimal:
	remainder = number_in_decimal % 2
	number_in_decimal = number_in_decimal // 2
	number_as_binary += str(remainder)

counter = 0
for symbol in number_as_binary:
	if state_of_binary == '0' and symbol == '0':
		counter += 1
	elif state_of_binary == '1' and symbol == '1':
		counter += 1

print(counter)
