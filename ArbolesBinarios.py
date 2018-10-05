# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class nodo:
	def __init__(self,value=None):
		self.valor=valor
		self.iz_hijo=None
		self.dere_hijo=None
class arbol_binario:
	def __init__(self):
		self.root=None

	def insertar(self,valor):
		if self.root==None:
			self.root=nodo(valor)
		else:
			self._insertar(valor,self.root)

	def _insertar(self,valor,actual_nodo):
		if valor<actual_nodo.valor:
			if actual_nodo.iz_hijo==None:
				actual_nodo.iz_hijo=nodo(valor)
				
			else:
				self._insertar(valor,actual_nodo.iz_hijo)
		elif valor>actual_nodo.valor:
			if actual_nodo.dere_hijo==None:
				actual_nodo.dere_hijo=nodo(valor)
				
			else:
				self._insertar(valor,actual_nodo.dere_hijo)
		else:
			print("El valor ya esta en el arbol")

	def imprimir_arbol(self):
		if self.root!=None:
			self._imprimir_arbol(self.root)

	def _imprimir_arbol(self,actual_nodo):
		if actual_nodo!=None:
			self._imprimir_arbol(actual_nodo.iz_hijo)
			print (str(actual_nodo.valor))
			self. _imprimir_arbol(actual_nodo.dere_hijo)

	def largo(self):
		if self.root!=None:
			return self._largo(self.root,0)
		else:
			return 0

	def _largo(self,actual_nodo,actual_largo):
		if actual_nodo==None: return actual_largo
		iz_largo=self._largo(actual_nodo.iz_hijo,actual_largo+1)
		dere_largo=self._largo(actual_nodo.dere_hijo,actual_largo+1)
		return max(iz_largo,dere_largo)

	def buscar(self,valor):
		if self.root!=None:
			return self._buscar(valor,self.root)
		else:
			return False

	def _buscar(self,valor,actual_nodo):
		if valor==actual_nodo.valor:
		    return True
                elif valor<actual_nodo.valor and actual_nodo.iz_hijo!=None:
		    return self._buscar(valor,actual_nodo.iz_hijo)
		elif valor>actual_nodo.valor and actual_nodo.dere_hijo!=None:
		    return self._buscar(valor,actual_nodo.dere_hijo)
		return False
	    
	def llenar_arbol(arbol,elem=30,ent_max=100):
                from radom import randint
                for _ in range(elem):
                    elem_actual=randint(0,ent_max)
                    arbol.insertar
                return arbol

        arbol=arbol_binario ()
        arbol=llenar_arbol(arbol)
        arbol.imprimir_arbol()
