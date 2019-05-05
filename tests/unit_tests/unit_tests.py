#!/usr/bin/env python3
import sys
import os
import unittest

sys.path.append('app')
from encryptor import *


class TestComponents(unittest.TestCase):

    def test_get_next_symbol(self):
        self.assertEqual('A', get_next_symbol('X', 3))
        return

    def test_caesar(self):
        with open('tests/unit_tests/test_data/caesar_input.txt', 'r') as processing_file:
            processing_text = processing_file.read()
        processing_text = caesar(processing_text, 313)
        with open('tests/unit_tests/test_data/caesar_expected.txt', 'r') as expected_file:
            expected_text = expected_file.read()
        self.assertEqual(processing_text, expected_text)
        pass

    def test_vigenere(self):
        with open('tests/unit_tests/test_data/vigenere_input.txt', 'r') as processing_file:
            processing_text = processing_file.read()
        processing_text = vigenere(processing_text, 'kanyewest', is_encoding=False)
        with open('tests/unit_tests/test_data/vigenere_expected.txt', 'r') as expected_file:
            expected_text = expected_file.read()
        self.assertEqual(processing_text, expected_text)
        pass

    def test_encode(self):
        process('caesar', 123, 'tests/unit_tests/test_data/encode_input.txt', 'output.txt', is_encoding=True)
        with open('output.txt', 'r') as result_file:
            result_text = result_file.read()
        with open('tests/unit_tests/test_data/encode_expected.txt', 'r') as expected_file:
            expected_text = expected_file.read()
        self.assertEqual(result_text, expected_text)
        os.remove('output.txt')
        return

    def test_decode(self):
        process('vigenere', 'drinkwater', 'tests/unit_tests/test_data/decode_input.txt', 'output.txt', is_encoding=False)
        with open('output.txt', 'r') as result_file:
            result_text = result_file.read()
        with open('tests/unit_tests/test_data/decode_expected.txt', 'r') as expected_file:
            expected_text = expected_file.read()
        self.assertEqual(result_text, expected_text)
        os.remove('output.txt')
        return

    def test_train(self):
        train('tests/unit_tests/test_data/train_input.txt', 'output.json')
        with open('output.json', 'r') as result_file:
            result_text = result_file.read()
        with open('tests/unit_tests/test_data/train_expected.json', 'r') as expected_file:
            expected_text = expected_file.read()
        self.assertEqual(result_text, expected_text)
        os.remove('output.json')
        return

    def test_hack(self):
        hack('tests/unit_tests/test_data/hack_input.txt', 'output.txt', 'tests/unit_tests/test_data/hack_model.json')
        with open('output.txt', 'r') as result_file:
            result_text = result_file.read()
        with open('tests/unit_tests/test_data/hack_expected.txt', 'r') as expected_file:
            expected_text = expected_file.read()
        self.assertEqual(result_text, expected_text)
        os.remove('output.txt')
        return


if __name__ == '__main__':
    unittest.main()
