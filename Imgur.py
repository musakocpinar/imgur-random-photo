import random
import string
import requests
import webbrowser

chrome_path = '/usr/bin/google-chrome %s'
url_1 = "https://api.imgur.com/post/v1/media/{}?client_id=546c25a59c58ad7&include=media%2Cadconfig%2Caccount"
url_2 = "https://i.imgur.com/{}.{}"

class Imgur():
    def __init__(self, extension: str = None):
        self.extension = extension
        self.with_api = extension is None

    def id_generator(self, size=7, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def generate_random_link(self):
        if self.with_api:
            return url_1.format(self.id_generator())
        else:
            return url_2.format(self.id_generator(), self.extension)

    def is_valid(self, link):
        resp = requests.get(link)

        if resp.status_code != 200:
            return False, None

        if self.with_api:
            resp_json = resp.json()

            if 'errors' in resp_json:
                if '404' not in resp_json['errors'][0]['code']:
                    raise Exception("Not handled error: {}".format(resp_json))
                return False, None
            else:
                return True, resp_json['media'][0]['url']
        else:
            if resp.url.endswith("https://i.imgur.com/removed.png"):
                return False, None
            else:
                return True, link


def open_in_browser(link):
    webbrowser.get(chrome_path).open(link)


def write_to_file(link, path='links.txt'):
    f = open(path, "a")
    f.write(link + "\n")
    f.close()