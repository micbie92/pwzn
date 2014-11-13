# -*- coding: utf-8 -*-
import math

import numpy as np


class Integrator(object):

    """
    Klasa która implementuje całki metodą Newtona Cotesa z użyciem interpolacji
    N-tego stopnia :math:`n\in<2, 11>`.

    Dodatkowe wymaganie: Ilość operacji wykonanych w kodzie Pythona nie może zależeć 
    od num_evaluations. Mówiąc potocznie: nie ma "fora".

    UWAGA: Zachęcam do użycia współczynników NC z zajęć numer 2. Można
    je pobrać od innego zespołu!

    Podpowiedź: nasz algorytm działa tak że najpierw dzieli przedział na
    N podprzedziałów a każdy całkuje metodą NC. Wektoryzacja całkowania
    podprzedziału jest prosta:

    >>> coefficients = np.asanyarray(self.PARAMS[7]) # Wspolczynniki NC
    >>> x = ... # Tutaj wyznaczacie wsółrzędne
    >>> res = (x * coefficients) * norma

    A czy da się stworzyć tablicę X tak by dało się policzyć jednym wywołaniem
    całkę dla wszystkich podprzedziałów?

    Podpowiedź II: Może być to trudne do uzyskania jeśli będziecie używać macierzy
    jednowymiarowej. Należy użyć broadcastingu.

    Podpowiedź III: Proszę o kontakt to podpowiem więcej.

    """

    PARAMS = {
        2: [1, 1],
        3: [1, 3, 1],
        4: [1, 3, 3, 1],
        5: [7, 32, 12, 32, 7],
        6: [19, 75, 50, 50, 75, 19],
        7: [41, 216, 27, 272, 27, 216, 41],
        8: [751, 3577, 1323, 2989, 2989, 1323, 3577, 751],
        9: [989, 5888, -928, 10496, -4540, 10496, -928, 5888, 989],
        10: [None] * 10,
        11: [None] * 11
    }

    PARAMS[10][0] = PARAMS[10][-1] = 2857
    PARAMS[10][1] = PARAMS[10][-2] = 15741
    PARAMS[10][2] = PARAMS[10][-3] = 1080
    PARAMS[10][3] = PARAMS[10][-4] = 19344
    PARAMS[10][4] = PARAMS[10][-5] = 5778

    PARAMS[11][0] = PARAMS[11][-1] = 16067
    PARAMS[11][1] = PARAMS[11][-2] = 106300
    PARAMS[11][2] = PARAMS[11][-3] = -48525
    PARAMS[11][3] = PARAMS[11][-4] = 272400
    PARAMS[11][4] = PARAMS[11][-5] = -260550
    PARAMS[11][5] = 427368

    def __init__(self, level):
        """
        Funkcja ta inicjalizuje obiekt do działania dla danego stopnia metody NC
        Jeśli obiekt zostanie skonstruowany z parametrem 2 używa metody trapezów.
        :param level: Stopień metody NC
        """
        self.level = level

    def integrate(self, func, func_range, num_evaluations):
        """

        :param callable func: Funkcja którą całkujemy
        :param tuple[int] func_range: Krotka zawierająca lewą i prawą granicę całkowania
        :param in tnum_evaluations:
        :return:
        """



if __name__ == "__main__":

    ii = Integrator(level=7)
    print(ii.integrate(np.sin, (0, np.pi), 30))
