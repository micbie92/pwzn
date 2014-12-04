# -*- coding: utf-8 -*-

from tasks.zaj5.zadanie2 import  load_data # Musi tu być żeby testy przeszły

import numpy as np


def get_event_count(data):
	"""

	Dane w pliku losowane są z takiego rozkładu:
	position, velocity: każda składowa losowana z rozkładu równomiernego 0-1
	mass: losowana z rozkładu równomiernego od 1 do 100.

	Zwraca ilość zdarzeń w pliku. Każda struktura ma przypisane do którego
	wydarzenia należy. Jeśli w pliku jest wydarzenie N > 0
	to jest i wydarzenie N-1.

	:param np.ndarray data: Wynik działania zadanie2.load_data
	"""
	
	return np.max(data['event_id'])


def get_center_of_mass(event_id, data):
	"""
	Zwraca macierz numpy zawierajacą położenie x, y i z środka masy układu.
	:param np.ndarray data: Wynik działania zadanie2.load_data
	:return: Macierz 3 x 1
	"""
	

	data = data[data['event_id']==event_id]
	return (data['particle_mass'][:,np.newaxis] * data['particle_position']).sum(axis=0) / (data['particle_mass']).sum()

def get_energy_spectrum(event_id, data, left, right, bins):
	"""
	Zwraca wartości histogramu energii kinetycznej cząstek (tak: (m*v^2)/2).
	:param np.ndarray data: Wynik działania zadanie2.load_data
	:param int left: Lewa granica histogramowania
	:param int right: Prawa granica historamowania
	:param int bins: ilość binów w historamie
	:return: macierz o rozmiarze 1 x bins

	Podpowiedż: np.histogram
	"""
	
	data = data[data['event_id']==event_id]

	en = data['particle_mass']/2*np.sqrt(data['particle_velocity'][:,0]**2 + data['particle_velocity'][:,1]**2 + data['particle_velocity'][:,2]**2)
	return (np.histogram(en, range=(left, right), bins=bins)[0])
	

if __name__ == "__main__":
	data = load_data("...")
	# print(data['velocity'])
#	print(get_event_count(data))
#	print(get_center_of_mass(1, data))
#	print(list(get_energy_spectrum(3, data, 0, 90, 100)))
