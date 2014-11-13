# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import numpy as np

__GOSPER_GUN = """
........................O...........
......................O.O...........
............OO......OO............OO
...........O...O....OO............OO
OO........O.....O...OO..............
OO........O...O.OO....O.O...........
..........O.....O.......O...........
...........O...O....................
............OO......................
"""


def shape_from_funny_string(data):
    data = data.strip()
    result = []
    for line in data.split():
        line = line.strip()
        line_as_arr = []

        for ch in line:
            if ch == '.':
                line_as_arr.append(0)
            elif ch == 'O':
                line_as_arr.append(1)
            else:
                raise ValueError("Invalid char " + ch)
        result.append(line_as_arr)
    return np.asarray(result, dtype=bool)

gosper_gun = shape_from_funny_string(__GOSPER_GUN)

square = np.ones((2, 2), dtype=bool)

beehive = np.asanyarray([
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
], dtype=bool)

blinker = np.asanyarray([
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
])