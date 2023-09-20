def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            offset = ord('a')
            result.append(chr(((ord(char) - offset + 13) % 26) + offset))
        elif 'A' <= char <= 'Z':
            offset = ord('A')
            result.append(chr(((ord(char) - offset + 13) % 26) + offset))
        else:
            result.append(char)
    return ''.join(result)

decrypted_text = rot13("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}")
print(decrypted_text)
