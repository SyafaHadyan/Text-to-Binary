text = "Text"
binary = ""
for char in text:
    ascii_value = ord(char)
    binary_value = bin(ascii_value)[2:].zfill(8)
    binary += binary_value
print(binary)
