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

    HISTO_B = [33, 15, 22, 16, 15, 14, 25, 28, 24, 17, 17, 18, 23, 19, 23, 27, 19, 25, 20, 18, 22, 13, 16, 18, 18, 18, 22, 18, 24, 20, 12, 11, 22, 14, 13, 20, 18, 18, 14, 18, 14, 12, 12, 10, 14, 11, 10, 13, 11, 4, 7, 6, 9, 12, 16, 7, 9, 7, 6, 3, 5, 7, 3, 3, 2, 1, 2, 3, 3, 1, 1, 2, 2, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    HISTO_A = [24, 22, 13, 20, 15, 22, 22, 17, 25, 19, 17, 18, 21, 18, 15, 21, 20, 25, 21, 26, 25, 13, 17, 15, 20, 21, 22, 16, 14, 19, 17, 18, 18, 15, 20, 17, 17, 11, 15, 15, 18, 13, 17, 7, 19, 7, 9, 10, 13, 10, 16, 11, 7, 11, 7, 5, 10, 8, 6, 8, 4, 6, 3, 4, 3, 3, 3, 1, 2, 3, 2, 2, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
