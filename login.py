import re
from memory_profiler import profile


ALLOWED_CHAR = ('-', '.')


def login(login_string: str) -> bool:
    length = len(login_string)
    if length > 20 or length <= 1:
        return False
    for char in login_string:
        if not char.isalpha():
            if not char.isdigit():
                if char not in ALLOWED_CHAR:
                    return False
    if login_string[-1].isalpha() and login_string[0].isalpha():
        return True
    else:
        return False


def re_login(login_string: str) -> bool:
    length = len(login_string)
    if length > 20 or length == 0:
        return False
    if re.findall(r'^[a-zA-Z][a-zA-Z0-9-.]*[a-zA-Z]$', login_string):
        return True
    else:
        return False


if __name__ == '__main__':
    profile(login('As-df.asdF'))
    profile(re_login('As-df.asdF'))
