from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle('Prueba PyQt5')
ventana.setGeometry(100, 100, 280, 80)
label = QLabel('¡PyQt5 está instalado correctamente!', ventana)
label.move(50, 30)
ventana.show()
sys.exit(app.exec_())