#!/usr/bin/env python3
import sys
import os
from common import *

sys.path.append('app')
from encryptor import *


def test_caesar_encode_decode():
    required_load = 5 * 10 ** 5
    key = random.randint(0, 10 ** 9)
    input_text = generate_text(required_load)
    with open('input.txt', 'w') as input_file:
        input_file.write(input_text)
    process('caesar', key, 'input.txt', 'output.txt', is_encoding=True)
    process('caesar', key, 'output.txt', 'output.txt', is_encoding=False)
    with open('output.txt', 'r') as result_file:
        assert input_text == result_file.read(), 'Caesar encoding-decoding is incorrect with large data'
    os.remove('output.txt')
    os.remove('input.txt')
    return


def test_vigenere_encode_decode():
    required_load = 5 * 10 ** 5
    key = generate_text(15)
    input_text = generate_text(required_load)
    with open('input.txt', 'w') as input_file:
        input_file.write(input_text)
    process('vigenere', key, 'input.txt', 'output.txt', is_encoding=True)
    process('vigenere', key, 'output.txt', 'output.txt', is_encoding=False)
    with open('output.txt', 'r') as result_file:
        assert input_text == result_file.read(), 'Vigenere encoding-decoding is incorrect with large data'
    os.remove('output.txt')
    os.remove('input.txt')
    return


def test_train_hack():
    input_text = ''
    with open('tests/load_tests/test_data/large_text.txt', 'r') as input_file:
        input_text = input_file.read()
    key = random.randint(0, 10 ** 9)
    process('caesar', key, 'tests/load_tests/test_data/large_text.txt', 'output.txt', is_encoding=True)
    train('tests/load_tests/test_data/large_text.txt', 'tests/load_tests/test_data/example_model.json')
    hack('output.txt', 'output.txt', 'tests/load_tests/test_data/example_model.json')
    with open('output.txt', 'r') as output_file:
        assert input_text == output_file.read(), 'Train-hack process is incorrect with large data'
    os.remove('output.txt')
    return
