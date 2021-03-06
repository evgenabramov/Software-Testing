#!/usr/bin/env python3
import sys
import os
import time
from common import *

sys.path.append('app')
from encryptor import *


def test_train_time():
    required_load = 5 * 10 ** 5
    text = generate_text(required_load)
    with open('input.txt', 'w') as input_file:
        input_file.write(text)
    start_time = time.time()
    train('input.txt', 'model.json')
    working_time = time.time() - start_time
    assert working_time < 1, 'Training time is too long'
    os.remove('input.txt')
    os.remove('model.json')
    return
