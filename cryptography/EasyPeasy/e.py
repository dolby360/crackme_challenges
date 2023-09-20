import pwn
from typing import List

p = pwn.remote("mercury.picoctf.net", 36981)
FLAG = "5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c"
FIRST_KEY_LEN = len(FLAG) // 2
FILLER = b"A" * (50000 - FIRST_KEY_LEN)
FLAG_AS_INTS = [int(FLAG[i:i+2], 16) for i in range(0, len(FLAG), 2)]

def cycle_to_the_beginning_of_the_key():
    p.readuntil("What data would you like to encrypt?")
    p.sendline(FILLER)

def get_encrypted_a_with_the_same_key_as_flag() -> List[str]:
    a = p.readuntil("What data would you like to encrypt?")
    p.sendline(b"A" * FIRST_KEY_LEN)
    output = p.readuntil("What data would you like to encrypt?")
    output = output.decode().split("\n")[1]
    return [output[i:i+2] for i in range(0, len(output), 2)]

def get_key_by_encrypted_a(encrypted_a: List[str]) -> List[int]:
    return [ord("A") ^ int(k, 16) for k in encrypted_a]

def decrypt_msg(key: List[int], msg: List[int]) -> str:
    dec = list(map(lambda x, y: chr(x ^ y), key, msg))
    return "".join(dec)

def main():
    cycle_to_the_beginning_of_the_key()
    encrypted_a = get_encrypted_a_with_the_same_key_as_flag()
    key = get_key_by_encrypted_a(encrypted_a)
    flag = decrypt_msg(key, FLAG_AS_INTS)
    print(flag)

if __name__ == "__main__":
    main()
