#!/usr/bin/env python3
import sys
import os
import time
from common import *

sys.path.append('app')
from encryptor import *


def test_encode_caesar_time():
    required_load = 5 * 10 ** 5
    text = generate_text(required_load)
    with open('input.txt', 'w') as input_file:
        input_file.write(text)
    start_time = time.time()
    process('caesar', random.randint(0, 10 ** 9), 'input.txt', 'output.txt', is_encoding=True)
    working_time = time.time() - start_time
    assert working_time < 1, 'Encoding time is too long for caesar cipher'
    os.remove('input.txt')
    os.remove('output.txt')
    return


def test_encode_vigenere_time():
    required_load = 5 * 10 ** 5
    text = generate_text(required_load)
    with open('input.txt', 'w') as input_file:
        input_file.write(text)
    start_time = time.time()
    process('vigenere', generate_text(15), 'input.txt', 'output.txt', is_encoding=True)
    working_time = time.time() - start_time
    assert working_time < 1, 'Encoding time is too long for vigenere cipher'
    os.remove('input.txt')
    os.remove('output.txt')
    return
