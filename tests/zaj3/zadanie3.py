# -*- coding: utf-8 -*-
import itertools
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
            # contents = map(itemgetter(0), zip(contents, range(3000)))
            contents = itertools.islice(contents, 3000)
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
        if not self.SHORT:
            for gram, freq in [(' of the', 85829), ('of the ', 81476), (' title ', 48402), ('in the ', 44836), (' in the', 44099), (' http w', 42149), (' ref na', 41358), ('f name ', 41356), ('ef name', 41352), ('ref nam', 41347), ('http ww', 38487), ('ttp www', 38466), ('tp www.', 38019), ('rl http', 35274), ('url htt', 35272), ('l http ', 33997), ('ublishe', 32234), ('publish', 31975), (' publis', 31822), (' url ht', 30714), ('blisher', 29641)]:
                with self.subTest(gram):
                    self.assertEqual(
                        self.ngrams[gram], freq)

    # def test_sha(self):
    #     out_file = tempfile.mktemp()
    #
    #     self.save_ngrams(
    #         out_file,
    #         self.ngrams)
    #
    #     sha = hashlib.sha256()
    #     with open(out_file, 'rb') as f:
    #         while True:
    #             res = f.read(4096)
    #             if len(res) == 0:
    #                 break
    #             sha.update(res)
    #
    #     self.assertEqual(
    #         sha.hexdigest(),
    #         '270fa3d327fed84d91b3f95ff787749a4004145968c4fab938ca36ae878457b8')
