from time import sleep
from PyQt5 import QtWidgets
import sys
import os

#Graphic interface
from .gui import Ui_MainWindow

from src.core import utils
from src.database import CNXNSQL
#Button signals
from src.signals import connectSignals


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class envGUI(QtWidgets.QMainWindow):
    def __init__(self):
        
        super(envGUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        ## Line to get new invoice number ##
        utils.newinvoicenumber(self)

        ## Button Signals ##
        connectSignals.buttonSignals(self)           
        

#ejecucion GUI
if __name__ == '__main__':

    CNXNSQL()
    app = QtWidgets.QApplication(sys.argv)
    GUI = envGUI()
    GUI.show()
    sys.exit(app.exec_())
