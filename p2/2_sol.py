import re

def read_hex_values_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    # Extract hexadecimal values
    hex_values = re.findall(r'0x[0-9A-Fa-f]+', content)
    # Convert hexadecimal strings to integers
    integers = [int(h, 16) for h in hex_values]
    return integers

def bytes_to_ints(hex_array):
    ints = []
    for i in range(0, len(hex_array), 8):
        value = 0
        for j in range(8):
            value |= (hex_array[i + j] << (j * 8))
        ints.append(value)
    return ints

# Read the hexadecimal values from the files
xs_hex = read_hex_values_from_file('xs.txt')
ys_hex = read_hex_values_from_file('ys.txt')

# Convert the hexadecimal byte arrays to integer arrays
xs = bytes_to_ints(xs_hex)
ys = bytes_to_ints(ys_hex)

# Ensure both arrays have the correct lengths
assert len(xs) == 4821
assert len(ys) >= 4821

# Calculate the accumulated sum of products
v5 = sum(xs[i] * ys[i] for i in range(4821))

# Convert the accumulated sum to a byte array
v5_bytes = v5.to_bytes((v5.bit_length() + 7) // 8, 'little')

# Convert the byte array to a string, ignoring non-printable characters
flag = ''.join(chr(b) if 32 <= b <= 126 else '' for b in v5_bytes)

print(f"The calculated flag is: ls{{{flag}}}")
