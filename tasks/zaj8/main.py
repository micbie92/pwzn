from qs import quicksort 
import timeit
import time

import pyximport; pyximport.install()
from cqs import cquicksort

import sys

import numpy as np

if __name__=="__main__":
	n=1
	if sys.argv[1:]:
		n = int( sys.argv[1] )

	tabs =  [ np.random.random_sample(10000000) for x in range(n) ]
	tabs2 = [ np.copy(tabs[i]) for i in range(n) ]

#	print(tabs)
	
	start = time.monotonic()
	for i in range(n):
		quicksort(tabs[i], 0, len(tabs[i])-1)
	pt = time.monotonic() - start
	print('python: mean time {}s'.format(pt/n))
	
	start = time.monotonic()
	for i in range(n):
#		print('a', len(tabs2[i]-1))
		cquicksort(tabs2[i], 0, len(tabs2[i])-1)
	ct = time.monotonic() - start
	print('cython: mean time {}s'.format(ct/n))
	
#	print(tabs)	
#	print(tabs2)
#	print( [ np.all(tabs[i] == tabs2[i]) for i in range(n) ] )
	print(np.all( [ np.allclose(tabs[i], tabs2[i], rtol=1e-6) for i in range(n) ] ) )
	
	print('speedup: {}x'.format(pt/ct))
