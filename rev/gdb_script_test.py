import gdb

gdb.execute('b *0x4006f7')
gdb.execute('r')

passwd = ''
for i in range(10):
    al = gdb.parse_and_eval('$al')
    passwd += chr(al)

    gdb.execute('set $bl = {}'.format(al))
    gdb.execute('continue')
    
print(passwd)