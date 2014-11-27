# -*- coding: utf-8 -*-
from contextlib import contextmanager
import csv
import unittest
import pathlib
import os
import tempfile
import numpy as np
import pickle
import base64


class TestClass(unittest.TestCase):

    TESTED_MODULE = None

    DATA_DIR = None


    def setUp(self):
        super().setUp()
        self.load_data = self.TESTED_MODULE.load_data


    @contextmanager
    def __tempfile(self):
        t = tempfile.mktemp()
        open(t, 'a').close()
        try:
            yield t
        finally:
            os.remove(t)

    def test_empty_file(self):
        with self.__tempfile() as f:
            with self.assertRaises(IOError):
                self.load_data(f)

    def test_too_small_file(self):
        for ii in range(30):
            with self.__tempfile() as f, self.subTest(ii), self.assertRaises(IOError):
                o = open(f, 'ab')
                o.write(b'*'*ii)
                o.close()
                self.load_data(f)

    def test_invalid_version(self):
        with self.__tempfile() as f, self.assertRaises(IOError):
            o = open(f, 'ab')
            o.write(b'6o\xfdo\xe2\xa4C\x90\x98\xb2t!\xbeurn\x08\x00\x03\x00:\x00\x00\x00\x00\x00\x1e\x00\x00\x00')
            o.close()
            self.load_data(f)

    def test_too_small_file_with_valid_header(self):
        with self.__tempfile() as f, self.assertRaises(IOError):
            o = open(f, 'ab')
            o.write(b'6o\xfdo\xe2\xa4C\x90\x98\xb2t!\xbeurn\x08\x00\x03\x00\x80\x00d\x00\x00\x00\x1e\x00\x00\x00')
            o.close()
            self.load_data(f)

    def test_ok_file(self):
        with self.__tempfile() as f:
            o = open(f, 'ab')
            o.write(b'6o\xfdo\xe2\xa4C\x90\x98\xb2t!\xbeurn\x03\x00\x03\x00\x80\x00d\x00\x00\x00\x96\x00\x00\x00xHUVZOtyoCrcIknvwNLGmisxTnkCGwnUnrejWdWlKNYCPGoMhHOEkkgxgRSldCTgWauzWlzOIhuVPzeiAvwwoEPTkeuPGJZWmrhiiZwXcJogaftLPXJnRGtj')
            o.write(b'\0' * (128*100))
            o.close()
            self.load_data(f)

    def test_bad_file(self):
        with self.__tempfile() as f, self.assertRaises(IOError):
            o = open(f, 'ab')
            o.write(b'6o\xfdo\xe2\xa4C\x90\x98\xb2t!\xbeurn\x03\x00\x03\x00\x80\x00d\x00\x00\x00\x96\x00\x00\x00xHUVZOtyoCrcIknvwNLGmisxTnkCGwnUnrejWdWlKNYCPGoMhHOEkkgxgRSldCTgWauzWlzOIhuVPzeiAvwwoEPTkeuPGJZWmrhiiZwXcJogaftLPXJnRGtj')
            o.write(b'\0' * (128*100 + 1))
            o.close()
            self.load_data(f)