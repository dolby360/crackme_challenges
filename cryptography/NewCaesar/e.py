import string

ALPHABET = string.ascii_lowercase[:16]
LOWERCASE_OFFSET = ord("a")

def reverse_b16_encode(enc: str):
    res = ""
    for i in range(0, len(enc), 2):
        first_item = enc[i]
        sec_item = enc[i + 1]
        left = ALPHABET.index(first_item)
        right =  ALPHABET.index(sec_item)
        res += chr((left << 4) | right)
    return res

def reverse_shift(sec_enc, key):
    ret = ""
    for c in sec_enc:
        ret += ALPHABET[ord(c) - ord(key)]
    return ret

if __name__ == "__main__":
    flag = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac" 
    for key in ALPHABET:
        print(reverse_b16_encode(reverse_shift(flag, key)))
