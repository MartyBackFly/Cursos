from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

import sys

# pip install PyQt5



from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Creador de archivos")
        self.setGeometry(100, 100, 600, 400)
        
        layout_principal = QVBoxLayout()

        layout_nombre = QHBoxLayout()
        lbl_nombre = QLabel("Nombre del archivo", self)
        entrada_nombre = QLineEdit(self)
        layout_nombre.addWidget(lbl_nombre)
        layout_nombre.addWidget(entrada_nombre)

        layout_contenido = QVBoxLayout()
        lbl_contenido = QLabel("Contenido del archivo", self)
        entrada_contenido = QTextEdit(self)
        layout_contenido.addWidget(lbl_contenido)
        layout_contenido.addWidget(entrada_contenido)

        btn_crear = QPushButton("Crear Archivo", self)
        
        layout_principal.addLayout(layout_nombre)
        layout_principal.addLayout(layout_contenido)
        layout_principal.addWidget(btn_crear)

        self.setLayout(layout_principal)

def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()