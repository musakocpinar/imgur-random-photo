import random
import string
import requests
import webbrowser

chrome_path = '/usr/bin/google-chrome %s'
url = "https://i.imgur.com/{}.{}"


def id_generator(size=7, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_random_link(extension='png'):
    return url.format(id_generator(), extension)


def is_valid(link):
    resp = requests.get(link)
    if resp.url.endswith("https://i.imgur.com/removed.png"):
        return False
    else:
        return True


def open_in_browser(link):
    webbrowser.get(chrome_path).open(link)


def write_to_file(link, path='links.txt'):
    f = open(path, "a")
    f.write(link + "\n")
    f.close()
