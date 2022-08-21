import random
import string
import requests
import webbrowser

chrome_path = '/usr/bin/google-chrome %s'
url = "https://api.imgur.com/post/v1/media/{}?client_id=546c25a59c58ad7&include=media%2Cadconfig%2Caccount"


def id_generator(size=7, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_random_link():
    return url.format(id_generator())


def is_valid(link):
    resp = requests.get(link)
    resp_json = resp.json()

    if 'errors' in resp_json:
        if '404' not in resp_json['errors'][0]['code']:
            raise Exception("Not handled error: {}".format(resp_json))
        return False, None
    else:
        return True, resp_json['media'][0]['url']


def open_in_browser(link):
    webbrowser.get(chrome_path).open(link)


def write_to_file(link, path='links.txt'):
    f = open(path, "a")
    f.write(link + "\n")
    f.close()
