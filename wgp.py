if __name__ == "__main__":
    import os
    import sys

    from PyQt6 import QtWidgets

    from views.main_window import Ui_MainWindow

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("wgp")

    if os.geteuid() != 0:
        QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Icon.Critical, "Error", "You need root privileges"
        ).exec()
        exit()
    else:
        ui = Ui_MainWindow()
        ui.show()
        app.exec()
