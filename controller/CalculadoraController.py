from PyQt5 import QtWidgets, uic
from service import CalculadoraService

class CalculadoraController:
    
    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frmcalculadora.ui")
        self.ventana.btncalcular.clicked.connect(self.onclickbtncalcular)
        self.ventana.show()
        app.exec()
    
    def onclickbtncalcular(self):
        resultado = 0
        operacion = ""
        try:
            num1 = int(self.ventana.txtnumero1.text())
            num2 = int(self.ventana.txtnumero2.text())
            if self.ventana.rbsuma.isChecked():
                resultado = CalculadoraService.suma(num1,num2)
                operacion = "Suma"
            elif self.ventana.rbresta.isChecked():
                resultado = CalculadoraService.resta(num1,num2)
                operacion = "Resta" 
            elif self.ventana.rbmultiplica.isChecked():
                resultado = CalculadoraService.multiplica(num1,num2)
                operacion = "Multiplica"
            elif self.ventana.rbdivide.isChecked():
                resultado = CalculadoraService.divide(num1,num2)
                operacion = "Divide"
            else:
                resultado = 0
                operacion = "Elegir operación"
        except:
            operacion = "Ingresar valores numéricos"
        finally:
            self.ventana.lblresultado.setText(operacion+" = " +
                                              str(resultado))