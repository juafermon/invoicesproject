from src.GUI.envGUI import envGUI
import sys
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = envGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()