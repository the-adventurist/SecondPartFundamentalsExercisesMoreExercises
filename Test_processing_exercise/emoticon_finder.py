text_ = input()

for current_symbol in range(len(text_)):
    if text_[current_symbol] == ":":
        print(f'{text_[current_symbol]}{text_[current_symbol + 1]}')
