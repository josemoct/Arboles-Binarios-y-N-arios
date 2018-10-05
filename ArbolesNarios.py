# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Nodo:
	def __init__(self, dato, par = None):
		self.dato = list([dato])
		self.padre = par
		self.hijo = list()
		
	def __str__(self):
		if self.padre:
			return str(self.padre.dato) + ' : ' + str(self.dato)
		return 'Root : ' + str(self.dato)
	
	def __lt__(self, nodo):
		return self.dato[0] < nodo.dato[0]
		
	def _esHoja(self):
		return len(self.hijo) == 0
			
	def _add(self, new_nodo):
		for hijo in new_nodo.hijo:
			hijo.padre = self
		self.dato.extend(new_nodo.dato)
		self.dato.sort()
		self.hijo.extend(new_nodo.hijo)
		if len(self.hijo) > 1:
			self.hijo.sort()
		if len(self.dato) > 2:
			self._separar()
	def _insertar(self, new_nodo):
		if self._esHoja():
			self._add(new_nodo)
		elif new_nodo.dato[0] > self.dato[-1]:
			self.hijo[-1]._insertar(new_nodo)
		else:
			for i in range(0, len(self.dato)):
				if new_nodo.dato[0] < self.dato[i]:
					self.hijo[i]._insertar(new_nodo)
					break
	def _separar(self):
		iz_hijo = Nodo(self.dato[0], self)
		dere_hijo = Nodo(self.dato[2], self)
		if self.hijo:
			self.hijo[0].padre = iz_hijo
			self.hijo[1].parent = iz_hijo
			self.hijo[2].parent = dere_hijo
			self.hijo[3].parent = dere_hijo
			iz_hijo.hijo = [self.hijo[0], self.hijo[1]]
			dere_hijo.hijo = [self.hijo[2], self.hijo[3]]
					
		self.hijo = [iz_hijo]
		self.hijo.append(dere_hijo)
		self.dato = [self.dato[1]]
		
		if self.padre:
			if self in self.padre.hijo:
				self.padre.hijo.remove(self)
			self.padre._add(self)
		else:
			iz_hijo.padre = self
			dere_hijo.padre = self
			
	def _encontrar(self, item):
		
		if item in self.dato:
			return item
		elif self._esHoja():
			return False
		elif item > self.dato[-1]:
			return self.hijo[-1]._encontrar(item)
		else:
			for i in range(len(self.dato)):
				if item < self.dato[i]:
					return self.hijo[i]._encontrar(item)
	def _remover(self, item):
		pass
	    	
	def _preorden(self):
		print (self) 
		for hijo in self.hijo:
			hijo._preorden()
class Arbol:
	def __init__(self):
		print("Tree __init__")
		self.root = None
		
	def insertar(self, item):
		print("Insertar en Arbol: " + str(item))
		if self.root is None:
			self.root = Nodo(item)
		else:
			self.root._insertar(Nodo(item))
			while self.root.padre:
				self.root = self.root.padre
		return True
	
	def encontrar(self, item):
		return self.root._encontrar(item)
		
	def remover(self, item):
		self.root.remover(item)
		
	def preorden(self):
		print ('----Preorder----')
		self.root._preorden()
		
arbol = Arbol()

lista = [43, 3, 2, 23, 1, 27, 8, 17, 89, 15, 8, 12, 5]

for item in lista:
	arbol.insertar(item)
arbol.preorden()
print (arbol.encontrar(5))