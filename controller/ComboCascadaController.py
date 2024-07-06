from PyQt5 import QtWidgets, uic

class ComboCascadaController:
    
    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frmcombocascada.ui")
        self.agregarGeneros()
        self.ventana.cbogenero.activated.connect(
            self.selectedCboGenero)
        self.ventana.cbonombres.activated.connect(
            self.selectedCboNombre)
        self.ventana.show()
        app.exec()
        
    def selectedCboNombre(self):
        if self.ventana.cbonombres.currentData() == "0":
            self.ventana.lblresultado.setText("Seleccione un nombre")
        else:
            self.ventana.lblresultado.setText(
                self.ventana.cbonombres.currentText())
    
    def selectedCboGenero(self):
        self.ventana.cbonombres.clear()
        self.ventana.lblresultado.setText("")
        if self.ventana.cbogenero.currentData() == "M":
            self.agregarNombresMasculino()
        elif self.ventana.cbogenero.currentData() == "F":
            self.agregarNombresFemenino()
        else:
            self.ventana.lblresultado.setText("Seleccione un género")
    
    def agregarGeneros(self):
        self.ventana.cbogenero.addItem("Seleccione", "0")
        self.ventana.cbogenero.addItem("Masculino", "M")
        self.ventana.cbogenero.addItem("Femenino", "F")
    
    def agregarNombresMasculino(self):
        self.ventana.cbonombres.addItem("Seleccione", "0")
        self.ventana.cbonombres.addItem("Carlos")
        self.ventana.cbonombres.addItem("Mario")
    
    def agregarNombresFemenino(self):
        self.ventana.cbonombres.addItem("Seleccione", "0")
        self.ventana.cbonombres.addItem("Lucia")
        self.ventana.cbonombres.addItem("Karla")