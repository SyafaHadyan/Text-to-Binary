def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits

input_text = input("Enter a string: ")
output_bits = text_to_bits(input_text)
print("Binary equivalent:", output_bits)
