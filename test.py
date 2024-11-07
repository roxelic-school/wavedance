alph = "abcdefghijklmnopqrstuvwxyz.!/[]();:0123456789"
char_to_num = {char: idx + 1 for idx, char in enumerate(alph)}
message = input("What message would you like to send: ").lower()
output_sequence = []
for char in message:
    if char == " ":
        output_sequence.append("0")
    elif char in char_to_num:
        output_sequence.append(str(char_to_num[char]))
    else:
        print(f"Character '{char}' cannot be typed.")
        output_sequence.append("?")
print("Numeric sequence to type:", " ".join(output_sequence))
