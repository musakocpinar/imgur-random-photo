from main import *

random_link = generate_random_link()
valid, imgur_link = is_valid(random_link)
if valid:
    open_in_browser(imgur_link)