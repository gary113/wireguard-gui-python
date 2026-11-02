from os import _exit, geteuid
from sys import argv

from PyQt6 import QtWidgets

from utility import language
from views.main import Ui_MainView

if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    app.setApplicationName("wgp")

    #Load the language selected by the user (system language by default)
    language.install_language(app, language.get_saved_language())

    if geteuid() != 0:
        err = QtWidgets.QApplication.translate("wgp", "Error")
        msg = QtWidgets.QApplication.translate("wgp", "You need root privileges")
        return_code = QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Icon.Critical, err, msg
        ).exec()

        _exit(return_code)
    else:
        ui = Ui_MainView()
        ui.show()
        return_code = app.exec()

        _exit(return_code)
