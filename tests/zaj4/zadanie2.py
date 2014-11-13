# -*- coding: utf-8 -*-
import pickle
import unittest
import math
import numpy as np
from tests.zaj4 import shapes


class TestClass(unittest.TestCase):

    TESTED_MODULE = None

    def setUp(self):
        super().setUp()
        self.calculate_neighbours = self.TESTED_MODULE.calculate_neighbours
        self.iterate = self.TESTED_MODULE.iterate

    def __test_board(self, board, expected, iterations=1, msg=None):
        result = np.asarray(board, dtype=bool)
        expected = np.asarray(expected, dtype=bool)
        for ii in range(iterations):
            result = self.iterate(result)

        with self.subTest("Check shape"):
            self.assertEqual(board.shape, result.shape)

        with self.subTest("Check dtype"):
            self.assertEqual(result.dtype, np.dtype(bool))

        MSG = ["Expected: ", str(expected), "got:", str(result), "board: ", str(board)]

        if msg:
            MSG.insert(0, msg)

        self.assertTrue(np.all(result == expected), "\n".join(MSG))

    def __test_neighbours(self, board, expected, msg=None):
        board = np.asarray(board, dtype=bool)
        result = np.copy(board)
        result = self.calculate_neighbours(result)

        with self.subTest("Check shape"):
            self.assertEqual(board.shape, result.shape)

        with self.subTest("Check dtype"):
            self.assertEqual(board.dtype, np.dtype(bool))

        MSG = ["Expected: ", str(expected), "got:", str(result), "board: ", str(board)]

        if msg:
            MSG.insert(0, msg)

        self.assertTrue(np.all(result == expected), "\n".join(MSG))

    def test_neighbours_empty(self):
        self.__test_neighbours(
            np.zeros((1000, 1000)),
            np.zeros((1000, 1000)),
            "Wyznaczamy sąsiadów w pustej tablicy")

    def test_neighbours_single_cell(self):
        single = np.zeros((3, 3))
        single[1, 1] = 1
        neighbours = np.ones((3, 3))
        neighbours[1, 1] = 0

        self.__test_neighbours(
            single,
            neighbours,
            "Wyznaczamy sąsiadów w tablicy 3x3 z jedną komórką w środku")

    def test_neighbours_full(self):
        BOARD = np.ones((3, 3))
        EXPECTED = np.asanyarray([
            [3, 5, 3],
            [5, 8, 5],
            [3, 5, 3],
        ])

        self.__test_neighbours(
            BOARD,
            EXPECTED,
            "Wyznaczamy sąsiadów w pęłnej 3x3")

    def test_gol_square(self):

        BOARD = np.zeros((9, 9), dtype=bool)
        BOARD[0:2, 0:2] = 1
        BOARD[-2:, -2:] = 1

        EXPECTED = BOARD

        N = 100

        self.__test_board(BOARD, EXPECTED, N,
            "Na planszy jest stablina strutura: kwadrat 2x2 sprawdzam czy nie zmieni się po 100 iteracjach")

    def test_gol_loaf(self):

        BOARD = shapes.beehive
        EXPECTED = shapes.beehive
        N = 100

        self.__test_board(BOARD, EXPECTED, N,
            "Na planszy jest inna stablina strutura: ul sprawdzam czy nie zmieni się po 100 iteracjach")

    def test_gol_blinker(self):

        BOARD = shapes.blinker
        EXPECTED = shapes.blinker
        N = 2


        self.__test_board(BOARD, EXPECTED, N,
            "Na planszy jest migacz, czyli struktura cykliczna o cylku 2, sprawdzam czy po dwóch iteracjach się nie zmieni")

    def test_gol_blinker2(self):

        BOARD = shapes.blinker
        EXPECTED = shapes.blinker
        N = 100


        self.__test_board(BOARD, EXPECTED, N,
            "Na planszy jest migacz, czyli struktura cykliczna o cylku 2, sprawdzam czy po 100 iteracjach się nie zmieni")

    def test_gol_blinker3(self):

        BOARD = shapes.blinker
        EXPECTED = shapes.blinker.T

        self.__test_board(BOARD, EXPECTED, 1,
            "Na planszy jest migacz, czyli struktura cykliczna o cylku 2, sprawdzam czy po jednej iteracji zmieni się odpowiednio")