import string
from random import sample


def get_random_string(length):
    return "tmp-" + ''.join(sample(string.ascii_lowercase + string.digits, length))
