"""
## ListWidget ##

Widget de listado y acceso a los archivos/data genetica provista en files. Cada item presenta los
siguientes campos al ser creados, modificados o leidos.

33: [family]
34: [genre]
35: [species_sci]
36: [species]
37: [group]
38: [route_img]
39: [desc]
40: [fasta]
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ListWidget(QWidget):
	def __init__(self):
		super().__init__()	# Llamada rutinaria al constructor del padre
		self.list = QListWidget()	# Lista
		self.list.setSelectionMode(QAbstractItemView.ExtendedSelection)
		self.items_list = []	# Lista de items (posible utilidad posterior)

		# Coneccion de accion->click de items al metodo 'self.itemSelected'
		self.list.itemClicked.connect(self.itemSelected)

		# Definicion del layout y adicion de la lista
		self.layout = QHBoxLayout()
		self.layout.addWidget(self.list)
		self.setLayout(self.layout)

		### <Pruebas>
		# for j in ["Tapaculo 1", "Tapaculo 2", "Tapaculo 3"]:
		#	self.addItem(j, "Perú", "posible_path.jpeg")
		### </Pruebas>

	def addItem(self, dict_values):
		group = dict_values['group']
		name = dict_values['species_sci']
		new_item = QListWidgetItem(group + "::" + name)	# Label del item en la lista
		fields = ['family','genre','species_sci', 'species', 'group', 'route_img', 'desc', 'fasta']
		for i, field in zip(range(33, 33+len(dict_values)), fields):
			new_item.setData(i, dict_values[field])	# new_item[33] = nombre de grupo/pais de procedencia de la especie
		self.list.addItem(new_item)	# Adicion del item
		self.items_list.append(new_item)	# Consideracion de la lista (posible utilidad futura)

	# Funcion de manejo de seleccion de item
	def itemSelected(self, item):
		pass
		#print("Clicked->{}:{}:{}".format(item.data(33), item.data(34), item.data(35)))