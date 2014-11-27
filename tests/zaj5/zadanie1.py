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

# Tak to jest obfuskacja kodu!
data = b'gANjbnVtcHkKZHR5cGUKcQBYAwAAAFYxMXEBSwBLAYdxAlJxAyhLA1gBAAAAfHEETlgFAAAAbmdyYW1xBVgEAAAAZnJlcXEGhnEHfXEIKGgFaABYAgAAAFM3cQlLAEsBh3EKUnELKEsDaAROTk5LB0sBSwB0cQxiSwCGcQ1oBmgAWAIAAAB1NHEOSwBLAYdxD1JxEChLA1gBAAAAPHERTk5OSv////9K/////0sAdHESYksHhnETdUsLSwFLEHRxFGIu'
dtype = pickle.loads(base64.b64decode(data))


class TestClass(unittest.TestCase):

    TESTED_MODULE = None

    DATA_DIR = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        load_data = cls.TESTED_MODULE.load_data
        if not cls.SHORT:
            cls.exc = None
            try:
                cls.data = load_data(str(pathlib.Path(cls.DATA_DIR, "zaj4", "enwiki-20140903-pages-articles_part_1.xmlascii.bin")))
            except Exception as e:
                cls.data = None
                cls.exc = e

    def setUp(self):
        super().setUp()
        self.load_data = self.TESTED_MODULE.load_data
        self.sugester = self.TESTED_MODULE.suggester

    @contextmanager
    def __tempfile(self):
        t = tempfile.mktemp()
        try:
            yield t
        finally:
            os.remove(t)

    def __convert(self, res):
        return [list(r) for r in res]

    def __check_result(self, input, data, expected, msg=None):

        with self.__tempfile() as t:

            mmap = np.memmap(t, dtype=dtype, mode='w+', shape=len(data))
            mmap['ngram'] = [d[0] for d in data]
            mmap['freq'] = [d[1] for d in data]
            mmap.flush()
            data = self.load_data(t)
            res = self.sugester(input, data)
            self.__assert_results(
                self.__convert(res), self.__convert(expected))

    def test_sugester_handmade(self):
        data = [["Kote", 1]]
        self.__check_result('Kot', data, [['e', 1.0]])

    def test_load_data(self):
        if self.SHORT:
            self.fail("Odpal pełne testy")
        if self.exc:
            raise ValueError("Błąd przy ładowaniu danych") from self.exc
        self.assertIsNotNone(self.data)

    def test_sugester_1(self):
        if not self.SHORT:
            self.assertEqual(self.sugester('ąęśłóź', self.data), [])

    # def test_sugester_2(self):
    #     if not self.SHORT:
    #         self.assertEqual(self.sugester('Rasput', self.data), [('i', 1.0)])

    def __assert_results(self, expected, result):
        try:
            for ii, (e, r) in enumerate(zip(expected, result)):
                self.assertEqual(r[0], e[0])
                self.assertAlmostEqual(r[1], e[1], places=3)
        except self.failureException as e:
            msg = "Twój wynik {}\n, Wynik oczekiwany {}\n".format(expected, result)
            raise AssertionError(msg) from e


    def test_sugester_3(self):
        if not self.SHORT:
            res = self.sugester('he end', self.data)
            self.__assert_results([(' ', 0.8473502765974505), (',', 0.03343221358133568), ('o', 0.03255030866672012), ('i', 0.022288142387557122), ('s', 0.01819931051070312), ('.', 0.01282770784895374)], res)

    def test_sugester_4(self):
        if not self.SHORT:
            res = self.sugester('in exc', self.data)
            self.__assert_results(self.SUG_4_OUT, res)

    SUG_4_OUT = [('h', 0.5969180859691808), ('e', 0.34144363341443634), ('l', 0.025952960259529603), ('a', 0.014598540145985401), ('i', 0.008921330089213302), ('r', 0.006488240064882401), ('u', 0.0024330900243309003), ('o', 0.0024330900243309003), (' ', 0.0008110300081103001)]
