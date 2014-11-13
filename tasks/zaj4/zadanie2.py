# -*- coding: utf-8 -*-

import numpy as np

from itertools import chain, permutations, product


def calculate_neighbours(board):

    """

    Funkcja zwraca tablicę która w polu N[R, C] zwraca ilość sąsiadów którą 
    ma komórka Board[R, C]. Za sąsiada uznajemy obszazoną komórkę po bokach lub
    na ukos od danej komórki, komórka nie jest swoim sąsiatem, zatem maksymalna
    ilość sąsiadów danej komórki wynosi 8.

    Funkcja ta powinna być zwektoryzowana, tj ilość operacji w bytekodzie
    Pythona nie powinna zależeć od rozmiaru macierzy.

    :param np.ndarray board: Dwuwymiarowa tablica zmiennych logicznych która
    obrazuje aktualny stan game of life. Jeśli w danym polu jest True (lub 1)
    oznacza to że dana komórka jest obsadzona


    Podpowiedź: Czy jest możliwe obliczenie ilości np. lewych sąsiadów
    których ma każda z komórek w macierzy, następnie liczymy ilość sąsiadów
    prawych itp.

    Podpowiedź II: Proszę uważać na komówki na bokach i rogach planszy.
    """
    m, n = board.shape
    board2 = np.zeros((m+2, n+2), dtype=int)
    board2[1:m+1, 1:n+1] = board.astype(int)
    wynik = np.zeros(board.shape, dtype=np.int)
    ones = np.ones(board.shape)
#    print(board)
#    print(board2[2:m+2, 1: n+1])
    for i, j in [ (1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1) ]:
        wynik += (ones * board2[1+i:m+1+i, 1+j:n+1+j]).astype(int)
#    print(board)
#    print(wynik)
#    print()
    return wynik

def iterate(board):

    """

    Funkcja pobiera planszę game of life i zwraca jej następną iterację.

    Zasady Game of life są takie:

    1. Komórka może być albo żywa albo martwa.
    2. Jeśli komórka jest martwa i ma trzech sąsiadóœ to ożywa.
    3. Jeśli komórka jest żywa i ma mniej niż dwóch sąsiadów to umiera,
       jeśli ma więcej niż trzech sąsiadóœ również umiera. W przeciwnym wypadku
       (dwóch lub trzech sąsiadów) to żyje dalej.

    :param np.ndarray board: Dwuwymiarowa tablica zmiennych logicznych która
    obrazuje aktualny stan game of life. Jeśli w danym polu jest True (lub 1)
    oznacza to że dana komórka jest obsadzona

    """
    from numpy import logical_and as land, logical_or as lor, logical_not as lnot
#    print(board)
    board = board.astype(np.bool)
    neigh = calculate_neighbours(board)
#    print(neigh)
    ozywa = land(board == False, neigh == 3)
    umiera = lnot(land( board == True, lor( neigh < 2, neigh > 3) ))
#    print(ozywa)
#    print(umiera)    
    board2 = land(lor(board, ozywa), umiera)
    return(board2)    
if __name__=="__main__":
    t=(np.random.randint(0, 10, (45,120)) > 5).astype(int)
#    calculate_neighbours(np.random.randint(0, 2,(10,10)))
#    iterate(t)

    import os
    import time
    while(True):
        os.system('clear')
        t2 = [ [ '#' if x else ' ' for x in y ] for y in t]
        t2 = '\n'.join( [ ''.join(x) for x in t2 ] )
        print(t2)
        t = iterate(t)
        time.sleep(0.1)
