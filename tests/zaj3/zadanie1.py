# -*- coding: utf-8 -*-
from contextlib import contextmanager
import csv
import unittest
import pathlib
import os
import sys
import tempfile


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
                cls.data = load_data(str(pathlib.Path(cls.DATA_DIR, "zaj3", "/opt/pwzn/zaj3/enwiki-20140903-pages-articles_part_2.xmlascii1000.csv")))
                cls.data = list(map(list, cls.data))
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
            with open(t, 'w') as f:
                w = csv.writer(f, dialect=csv.unix_dialect)
                w.writerows(data)
            data = self.load_data(t)
            res = self.sugester(input, data)
            self.__assert_results(
                self.__convert(res), self.__convert(expected))

    def test_sugester_handmade(self):
        data = [["Kotek", 1]]
        self.__check_result('Kot', data, [['e', 1.0]])

    def test_sugester_handmade_1(self):
        data = [["Ala ma k", 1], ["Aladyn", 1], ["Ale czemu nie działa", 1]]
        self.__check_result('Al', data, [['a', 0.66666], ['e', 0.33333]])

    def test_load_data(self):
        if self.SHORT:
            self.fail("Odpal pełne testy")
        if self.exc:
            raise ValueError("Błąd przy ładowaniu danych") from self.exc
        self.assertIsNotNone(self.data)

    def test_sugester_1(self):
        if not self.SHORT:
            self.assertEqual(self.sugester('ąęśłóź', self.data), [])

    def test_sugester_2(self):
        if not self.SHORT:
            self.assertEqual(self.sugester('pytho', self.data), [('n', 1.0)])

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
            res = self.sugester('Adel', self.data)
            self.__assert_results([('m', 0.4727272727272727), ('a', 0.3090909090909091), ('p', 0.07272727272727272)], res)

    def test_sugester_4(self):
        if not self.SHORT:
            res = self.sugester('oba', self.data)
            self.__assert_results(self.SUG_4_OUT, res)

    def test_sugester_5(self):
        if not self.SHORT:
            res = self.sugester('Oba', self.data)
            self.__assert_results(self.SUG_5_OUT, res)

    SUG_4_OUT = [('l', 0.30735930735930733), ('b', 0.2792207792207792),
                 ('c', 0.262987012987013), (' ', 0.03571428571428571),
                 ('r', 0.03354978354978355), ('s', 0.0183982683982684)]

    SUG_5_OUT = [('m', 0.9148936170212766), ('n', 0.0425531914893617), ('i', 0.02127659574468085), ('d', 0.02127659574468085)]
