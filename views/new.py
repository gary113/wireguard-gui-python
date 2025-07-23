from PyQt6 import QtCore, QtWidgets

from utility.functions import *


class Ui_NewView(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName("NewWindow")
        self.resize(600, 400)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel
            | QtWidgets.QDialogButtonBox.StandardButton.Ok
        )

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 3)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 2, 0, 1, 3)

        ####

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_publickey)
        self.timer.setInterval(UPDATE_INTERVAL)
        self.timer.start()

        ####

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(
            QtCore.QCoreApplication.translate("NewWindow", "Dialog", None)
        )
        self.label.setText(
            QtCore.QCoreApplication.translate("NewWindow", "Interface name", None)
        )
        self.label_2.setText(
            QtCore.QCoreApplication.translate("NewWindow", ".conf", None)
        )
        self.label_3.setText(
            QtCore.QCoreApplication.translate("NewWindow", "Public key", None)
        )

    def update_publickey(self):
        if "privatekey" in self.plainTextEdit.toPlainText().lower():
            publickey = get_specific_config_interface(
                self.plainTextEdit.toPlainText(), "publickey"
            )
            self.lineEdit_2.setText(publickey)
