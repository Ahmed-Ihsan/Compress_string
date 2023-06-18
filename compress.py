def run_length_encode(string):
    encoded_data = ""
    count = 1
    prev_char = string[0]

    # Apply Run-Length Encoding
    for char in string[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded_data += str(count) + prev_char
            count = 1
            prev_char = char

    encoded_data += str(count) + prev_char

    return encoded_data


def compress_string(string):
    compressed_data = ""
    count = 1
    prev_char = string[0]

    # Compress the string
    for char in string[1:]:
        if char == prev_char:
            count += 1
        else:
            compressed_data += prev_char + str(count)
            count = 1
            prev_char = char

    compressed_data += prev_char + str(count)

    return compressed_data


def convert_to_ascii(string):
    ascii_data = [ord(char) for char in string]
    return ascii_data


def convert_to_binary(data):
    binary_data = "".join(format(byte, "08b") for byte in data)
    return binary_data


def run_length_decode(encoded_data):
    decoded_data = ""
    i = 0
    while i < len(encoded_data):
        count = ""
        while i < len(encoded_data) and encoded_data[i].isdigit():
            count += encoded_data[i]
            i += 1
        char = encoded_data[i]
        decoded_data += char * (int(count) if count else 1)
        i += 1
    return decoded_data


def decompress_string(compressed_string):
    decompressed_data = ""
    i = 0
    while i < len(compressed_string):
        char = compressed_string[i]
        count = ""
        i += 1
        while i < len(compressed_string) and compressed_string[i].isdigit():
            count += compressed_string[i]
            i += 1
        decompressed_data += char * (int(count) if count else 1)
    return decompressed_data


def decode_binary(binary_data):
    ascii_data = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        ascii_data.append(int(byte, 2))
    return ascii_data


# Example usage
original_string = "ZZZZZZZ"
rle_encoded_string = run_length_encode(original_string)
compressed_string = compress_string(original_string)
ascii_data = convert_to_ascii(compressed_string)
binary_data = convert_to_binary(ascii_data)
decoded_string = run_length_decode(rle_encoded_string)
decompressed_string = decompress_string(compressed_string)

print("Original string:", original_string)
print("RLE encoded string:", rle_encoded_string)
print("Compressed string:", compressed_string)
print("ASCII representation:", ascii_data)
print("Binary representation:", binary_data)
print("Decoded string:", decoded_string)
print("Decompressed string:", decompressed_string)
