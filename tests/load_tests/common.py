import random
import string


def generate_text(size):
    return ''.join(
        random.choices(string.ascii_lowercase + string.ascii_uppercase + ' ' + '\n' + string.punctuation + string.digits, k=size))
