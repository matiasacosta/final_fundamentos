import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from controladores.controlador_menu_principal import ControladorMenuPrincipal

def mostrar_ventana():
    app = QApplication(sys.argv)
    ventana = ControladorMenuPrincipal()
    ventana.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    mostrar_ventana()