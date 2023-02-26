
def int8_wraparound(num, add):
    sum = (num + add)
    if sum <= 127:
        return sum
    base = -128
    if sum % 128 == 0:
        base = 0
    return (sum % 128) + base

def uint64_wraparound(num):
    return num & 0xffffffffffffffff

def key_gen(user_name):
    user_name = [ord(c) for c in user_name]
    for i in range(len(user_name)):
        user_name[i] = int8_wraparound(user_name[i], (i + 1 ^ 0x30))
    for i in range(len(user_name)):
        user_name[i] = int8_wraparound(user_name[i], (i & 0x10))
    for i in range(len(user_name)):
        user_name[i] = int8_wraparound(user_name[i], 126)
    temp_arr = [int8_wraparound(i * 5, 0) for i in user_name]
    concatenated = user_name + temp_arr
    num = 0
    for i in range(len(concatenated)):
        num += i*i + concatenated[i]

    uVar12 = uint64_wraparound((num >> 0x1e ^ num) * 13787848793156543929)
    uVar12 = uint64_wraparound((uVar12 >> 0x1b ^ uVar12) * 10723151780598845931)
    return uint64_wraparound(uVar12 >> 0x1f ^ uVar12)

print(key_gen("dolev"))
