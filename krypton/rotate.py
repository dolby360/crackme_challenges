import tqdm


def rotate_letters(text, n):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        else:
            result += char
    return result


input_text = "YRIRY GJB CNFFJBEQ EBGGRA"
for i in tqdm.tqdm(range(0,26)):
    rotated_text = rotate_letters(input_text, i)
    print(i)
    print(rotated_text)
    print("===========")
