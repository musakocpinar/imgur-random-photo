from main import *

random_link = generate_random_link()
is_valid = is_valid(random_link)
if is_valid:
    open_in_browser(random_link)