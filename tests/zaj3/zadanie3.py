# -*- coding: utf-8 -*-
from collections import defaultdict
import csv
import unittest
import pathlib
from operator import itemgetter
from tasks.zaj3.zadanie3 import iter_over_contents
import tempfile
import hashlib
import os


def load_data(path):
    """
    # WARN: Tak to jest rozwiązanie poprzedniego zadania!
    """
    keys = []
    frequencies = []

    with open(path, encoding='utf-8') as f:
        wr = csv.reader(f, dialect=csv.unix_dialect)
        for row in wr:
            keys.append(row[0])
            frequencies.append(int(row[1]))

    return keys, frequencies


class TestClass(unittest.TestCase):

    TESTED_MODULE = None

    DATA_DIR = None

    result = []

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        generate_ngrams = cls.TESTED_MODULE.generate_ngrams
        if not cls.SHORT:
            contents = iter_over_contents(str(pathlib.Path(cls.DATA_DIR, "zaj3", "enwiki-20140903-pages-articles_part_0.xml.bz2")))
            cls.ngrams = generate_ngrams(contents, 7)

    def setUp(self):
        super().setUp()
        self.generate_ngrams = self.TESTED_MODULE.generate_ngrams
        self.save_ngrams = self.TESTED_MODULE.save_ngrams

    def test_type(self):

        self.assertTrue(
            isinstance(self.generate_ngrams([("foo", "Ala ma kota")], 1),
                       (dict, defaultdict)), "Funkcja ta musi zwracać słownik")

    def test_simple(self):
        self.assertEqual(
            dict(self.generate_ngrams([("foo", "Ala ma kota")], 1)),
            {'a': 3, 'o': 1, 'm': 1, 'A': 1, ' ': 2, 'k': 1, 'l': 1, 't': 1}, )

    def test_equality(self):
        self.assertEqual(
            dict(self.generate_ngrams([("foo", "Ala ma kota")], 1)),
            dict(self.generate_ngrams([("foo", a) for a in ['Ala', 'ma', 'kota', '  ']], 1)))

    def test_3gram(self):
        self.assertEqual(
            dict(self.generate_ngrams([("foo", "Ala ma kota a Marta ma Asa")], 3)),
            {'la ': 1, 'Asa': 1, 'ma ': 2, 'Mar': 1, 'a A': 1, 'art': 1, 'Ala': 1, ' ma': 2, ' As': 1, 'a k': 1, 'ta ': 2, 'rta': 1, 'kot': 1, 'a m': 2, ' a ': 1, ' Ma': 1, 'ota': 1, 'a a': 1, ' ko': 1, 'a M': 1})

    def test_long(self):
        if self.SHORT:
            self.fail("By uzyskać ocenę odpal pełne testy")

    def test_most_popular(self):
        for gram, freq in [(' of the', 562580), ('of the ', 534684), (' title ', 309060), ('in the ', 292861), (' in the', 287172), (' http w', 266237), ('f name ', 259296), (' ref na', 259287), ('ef name', 259247), ('ref nam', 259223), ('http ww', 253221), ('ttp www', 253116), ('tp www.', 250037), ('rl http', 218080), ('url htt', 218063), ('l http ', 213962), ('ublishe', 208728), ('publish', 206973), (' publis', 205873), (' url ht', 204023), ('blisher', 190072), ('lisher ', 185805), ('ion of ', 183989), (' first ', 179979), ('. ref n', 174057)]:
            with self.subTest(gram):
                self.assertEqual(
                    self.ngrams[gram], freq)

    def test_sha(self):
        out_file = tempfile.mktemp()

        self.save_ngrams(
            out_file,
            self.ngrams)

        sha = hashlib.sha256()
        with open(out_file, 'rb') as f:
            while True:
                res = f.read(4096)
                if len(res) == 0:
                    break
                sha.update(res)

        self.assertEqual(
            sha.hexdigest(),
            '270fa3d327fed84d91b3f95ff787749a4004145968c4fab938ca36ae878457b8')
