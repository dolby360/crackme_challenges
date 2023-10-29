import json
import base64

def get_data():
    data = {
        "showpassword" : "no", 
        "bgcolor":"#ffffff"
    }
    json_string = json.dumps(data)
    return json_string

def calc_key(data: str):
    pass

def decode(s = "0l;$$98-8=?#9*jvi 'ngl*+(!$#9lrnh~x|{~xn67"):
    key = [78, 72, 76, 75]
    j = 3
    ret = ""
    
    for i in s:
        ret += chr(ord(i) ^ key[j])
        j = (j + 1) % len(key)
    return ret


def encode():
    key = [78, 72, 76, 75]
    j = 0
    enc = ""
    s = "yes" + "\", \"bgcolor\": \"#ffffff\"}"
    for i in s:
        enc += chr(ord(i) ^ key[j])
        j = (j + 1) % len(key)
    data = f"0l;$$98-8=?#9*jvi{enc}"
    print(data)
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

# print(get_data())
print(encode())
print(decode("0l;$$98-8=?#9*jvi7-?ibhn))+#'!:nqnjo-(.*-(j1"))
