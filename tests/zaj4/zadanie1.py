# -*- coding: utf-8 -*-
import unittest

import numpy as np

class TestClass(unittest.TestCase):

    TESTED_MODULE = None

    def setUp(self):
        super().setUp()
        self.linear_func = self.TESTED_MODULE.linear_func
        self.chisquared = self.TESTED_MODULE.chisquared
        self.least_sq = self.TESTED_MODULE.least_sq

    def test_linear_func(self):
        self.assertTrue(
            np.all(self.linear_func(np.linspace(0, 10, 50), 3, 10,) ==
                3 * np.linspace(0, 10, 50) + 10),
            "Funkcja liniowa nie działa poprawnie"
        )

    def test_chisquared(self):
        x = np.linspace(0, 10, 50)
        y = x * 3 + 10 + np.random.random(50)
        sigma_y = np.ones_like(y)
        data = np.vstack((x, y, sigma_y)).T
        sum = self.chisquared(data, 3, 10)
        self.assertLess(sum, 50)

    def test_leastsq(self):
        x = [2, 4, 6, 8, 10]
        y = [42, 48.4, 51.3, 56.3, 58.6]
        sigma_y = np.ones_like(y)
        data = np.vstack((x, y, sigma_y)).T
        a, b = self.least_sq(data)
        self.assertAlmostEqual(38.99, a, places=2)
        self.assertAlmostEqual(2.055, b, places=2)