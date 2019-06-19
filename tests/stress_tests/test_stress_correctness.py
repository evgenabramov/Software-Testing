#!/usr/bin/env python3
import sys
import os
import random

sys.path.append('app')
from encryptor import *


def test_caesar_encode_decode():
    key = random.randint(0, 10 ** 9)
    process('caesar', key, 'tests/stress_tests/test_data/generous_text.txt', 'output.txt', is_encoding=True)
    process('caesar', key, 'output.txt', 'output.txt', is_encoding=False)
    with open('output.txt', 'r') as result_file, open('tests/stress_tests/test_data/generous_text.txt',
                                                      'r') as input_file:
        assert input_file.read() == result_file.read(), 'Caesar encoding-decoding is incorrect with text of 51906498 letters'
    os.remove('output.txt')
    return


def test_vigenere_encode_decode():
    key = 'verylongstringwithletters'
    process('vigenere', key, 'tests/stress_tests/test_data/generous_text.txt', 'output.txt', is_encoding=True)
    process('vigenere', key, 'output.txt', 'output.txt', is_encoding=False)
    with open('output.txt', 'r') as result_file, open('tests/stress_tests/test_data/generous_text.txt',
                                                      'r') as input_file:
        assert input_file.read() == result_file.read(), 'Vigenere encoding-decoding is incorrect with text of 51906498 letters'
    os.remove('output.txt')
    return


def test_train_hack():
    with open('tests/stress_tests/test_data/generous_text.txt', 'r') as input_file:
        input_text = input_file.read()
    key = random.randint(0, 10 ** 9)
    process('caesar', key, 'tests/stress_tests/test_data/generous_text.txt', 'output.txt', is_encoding=True)
    train('tests/stress_tests/test_data/generous_text.txt', 'tests/stress_tests/test_data/model.json')
    hack('output.txt', 'output.txt', 'tests/stress_tests/test_data/model.json')
    with open('output.txt', 'r') as output_file:
        assert input_text == output_file.read(), 'Train-hack process is incorrect with text of 51906498 letters'
    os.remove('output.txt')
    return
