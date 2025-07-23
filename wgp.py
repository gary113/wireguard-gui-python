from os import _exit, geteuid
from sys import argv

from PyQt6 import QtWidgets

from views.main import Ui_MainView

if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    app.setApplicationName("wgp")

    if geteuid() != 0:
        return_code = QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Icon.Critical, "Error", "You need root privileges"
        ).exec()

        _exit(return_code)
    else:
        ui = Ui_MainView()
        ui.show()
        return_code = app.exec()

        _exit(return_code)
