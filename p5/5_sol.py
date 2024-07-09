import re

def read_alphabet_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    hex_values = re.findall(r'0x[0-9A-Fa-f]+', content)
    alphabet = [int(h, 16) for h in hex_values]
    return alphabet

alphabet = read_alphabet_from_file('alphabet.txt')

memo = {}
def a(n):
    if n in memo:
        return memo[n]
    if n <= 3:
        result = n
    else:
        result1 = a(n - 1)
        result2 = a(n - 2)
        result3 = a(n - 3)
        result = result1 + result2 + result3
    memo[n] = result
    return result

def b(n):
    return a(n)

def generate_key():
    key = ""
    for i in range(14):
        index = b(i * 8)
        key += chr(alphabet[index % len(alphabet)])
        # print(key)
    return key

full_key = generate_key()
print(f"Full key: {full_key}")
