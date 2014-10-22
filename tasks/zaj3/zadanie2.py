# -*- coding: utf-8 -*-
import csv

def merge(path1, path2, out_file):
	"""
	Funkcja pobiera nazwy dwóch plików z n-gramami (takie jak w poprzedmim
	zadaniu) i łączy zawartość tych plików i zapisuje do pliku w ścieżce ``out``.

	Pliki z n-gramami są posortowane względem zawartości n-grama.

	:param str path1: Ścieżka do pierwszego pliku
	:param str path2: Ścieżka do drugiego pliku
	:param str out_file:  Ścieżka wynikowa

	Testowanie tej funkcji na pełnych danych może być mało wygodne, możecie
	stworzyć inną funkcję która działa na dwóch listach/generatorach i testować
	ją.

	Naiwna implementacja polegałaby na stworzeniu dwóch słowników które
	zawierają mapowanie ngram -> ilość wystąpień i połączeniu ich.

	Lepsza implementacja ładuje jeden z plików do pamięci RAM (jako słownik
	bądź listę) a po drugim iteruje.

	Najlepsza implementacja nie wymaga ma złożoność pamięciową ``O(1)``.
	Podpowiedź: merge sort. Nie jest to trywialne zadanie, ale jest do zrobienia.
	"""
	
	from collections import defaultdict
	d = defaultdict(lambda: 0)
	
	with open(path1, 'r') as f:
		r = csv.reader(f, dialect=csv.unix_dialect)
		for line in r:
			d[line[0]]=int(line[1])
		
	with open(path2, 'r') as f:
		r = csv.reader(f, dialect=csv.unix_dialect)
		for (ngram, n) in r:
			d[ngram] += int(n)
			
	with open(out_file, 'w') as f:
		w = csv.writer(f, dialect=csv.unix_dialect)
		w.writerows(sorted(d.items(), key = lambda x: x[0]))

if __name__ == '__main__':

	merge(
		'/opt/pwzn/zaj3/enwiki-20140903-pages-articles_part_0.xmlascii.csv',
		'/opt/pwzn/zaj3/enwiki-20140903-pages-articles_part_1.xmlascii.csv',
		'mergeout.csv')
