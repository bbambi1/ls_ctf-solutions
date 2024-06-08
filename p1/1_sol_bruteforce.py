import subprocess
import string
import sys

def interact_with_executable(input_string):
    # This function interacts with the executable and returns its output
    process = subprocess.Popen(['./1_speak_friend'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(input=input_string.encode())
    return stdout.decode()

# def interact_with_executable_verbose(input_string):
#     # This function interacts with the executable and returns its output
#     process = subprocess.Popen(
#         ['./1_speak_friend'], 
#         stdin=subprocess.PIPE, 
#         stdout=subprocess.PIPE, 
#         stderr=subprocess.PIPE, 
#         text=True
#     )
#     stdout, stderr = process.communicate(input=input_string)
#     sys.stdout.write(stdout)
#     sys.stderr.write(stderr)
#     return stdout

def parse_output(output):
    lines = output.split('\n')
    for line in lines:
        if '>>' in line:
            return line.split('>> ')[-1]
    return ''

# Define the characters to try
possible_chars = string.ascii_letters + string.digits + string.punctuation + ' '

# Initialize the flag with unknown parts
flag_length = 28
flag = ['*'] * flag_length

def brute_force_flag():
    # Dictionary to keep track of working characters for each position
    working_characters = {}

    for i in range(flag_length):
        for char in possible_chars:
            test_input = ''.join(flag[:i]) + char + ''.join(flag[i+1:])
            print(f"Testing input: {test_input}")
            output = interact_with_executable(test_input)
            revealed_flag = parse_output(output)
            if len(revealed_flag) == flag_length and revealed_flag[i] != '*':
                flag[i] = revealed_flag[i]
                print(f"Updated flag: {''.join(flag)}")
                # Store the working character for the current position
                working_characters[i] = char
                break

    # Generate the final input to reveal the full flag
    final_input = ''.join(working_characters.get(i, '*') for i in range(flag_length))
    print(f"Final input to reveal the flag: {final_input}")
    return final_input

# Start brute-forcing the flag
final_input = brute_force_flag()

# Print the final flag
print(f"Final flag: {''.join(flag)}")
