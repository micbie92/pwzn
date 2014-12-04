# -*- coding: utf-8 -*-

import unittest
import pathlib

class TestClass(unittest.TestCase):

    TESTED_MODULE = None

    DATA_DIR = None


    def setUp(self):
        self.load_data = self.TESTED_MODULE.load_data
        self.get_event_count = self.TESTED_MODULE.get_event_count
        self.get_center_of_mass = self.TESTED_MODULE.get_center_of_mass
        self.get_energy_spectrum = self.TESTED_MODULE.get_energy_spectrum

        self.dataA = self.load_data(str(pathlib.Path(self.DATA_DIR, "zaj5", "zadA")))
        self.dataB = self.load_data(str(pathlib.Path(self.DATA_DIR, "zaj5", "zadB")))

    def test_event_countA(self):
        self.assertEqual(self.get_event_count(self.dataA), 1)

    def test_event_countB(self):
        self.assertEqual(self.get_event_count(self.dataB), 10000)

    def test_center_of_mass_a(self):

        com = self.get_center_of_mass(1, self.dataA)

        for ii, val in enumerate([ 0.49724573,  0.52034831,  0.49950778]):
            self.assertAlmostEqual(com[ii], val)

    def test_center_of_mass_b(self):

        com = self.get_center_of_mass(3, self.dataB)

        for ii, val in enumerate([0.46980596, 0.49875301, 0.50159389]):
            self.assertAlmostEqual(com[ii], val)

    def test_histogram_a(self):

        com = self.get_energy_spectrum(1, self.dataA, 0, 90, 100)

        for ii, val in enumerate(self.HISTO_A):
            self.assertAlmostEqual(com[ii], val)

    def test_histogram_b(self):

        com = self.get_energy_spectrum(3, self.dataB, 0, 90, 100)

        for ii, val in enumerate(self.HISTO_B):
            self.assertAlmostEqual(com[ii], val)

    HISTO_B = [42, 20, 26, 25, 20, 25, 26, 28, 26, 30, 30, 14, 11, 23, 19, 22, 17, 18, 15, 16, 15, 19, 13, 17, 20, 15, 16, 16, 10, 15, 19, 11, 13, 18, 12, 9, 15, 8, 10, 11, 7, 6, 13, 13, 13, 9, 7, 4, 10, 11, 6, 5, 9, 5, 9, 4, 4, 13, 5, 7, 8, 6, 2, 7, 4, 4, 0, 5, 6, 4, 1, 0, 4, 3, 3, 6, 2, 3, 6, 2, 3, 1, 2, 0, 4, 1, 3, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 3]

    HISTO_A = [35, 29, 20, 21, 31, 25, 30, 21, 25, 15, 22, 23, 23, 24, 22, 17, 21, 17, 11, 11, 17, 15, 19, 11, 17, 19, 21, 19, 11, 14, 9, 13, 18, 12, 8, 14, 12, 12, 10, 10, 14, 15, 5, 7, 10, 13, 9, 11, 11, 3, 7, 12, 10, 8, 8, 6, 2, 8, 7, 3, 3, 9, 9, 6, 7, 2, 3, 6, 3, 6, 1, 3, 3, 5, 3, 2, 3, 0, 1, 2, 3, 3, 1, 0, 0, 3, 4, 1, 0, 1, 1, 2, 3, 0, 0, 0, 0, 0, 0, 1]
