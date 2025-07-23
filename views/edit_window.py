from PyQt6 import QtCore, QtWidgets

from utility.functions import *


class Ui_EditWindow(QtWidgets.QDialog):

    def __init__(self, interface):
        super().__init__()
        self.setupUi(interface)

    def setupUi(self, interface):
        if not self.objectName():
            self.setObjectName("EditWindow")
        self.resize(600, 400)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 2)

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel
            | QtWidgets.QDialogButtonBox.StandardButton.Ok
        )

        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 2)

        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setObjectName("textEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 2, 0, 1, 3)

        ######
        self.interface = interface

        self.plainTextEdit.insertPlainText(
            get_config_file_content(self.interface)["full_content"]
        )
        self.lineEdit.setText(
            get_specific_config_interface(
                get_config_file_content(self.interface)["interface_content"],
                "publickey",
            )
        )
        self.lineEdit_2.setText(get_interface_name(self.interface))

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_publickey)
        self.timer.setInterval(UPDATE_INTERVAL)
        self.timer.start()
        ######

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("EditWindow", "Edit"))
        self.label.setText(_translate("EditWindow", "Public key"))
        self.label_2.setText(_translate("EditWindow", "Interface name", None))
        self.label_3.setText(_translate("EditWindow", ".conf", None))

    def update_publickey(self):
        if "privatekey" in self.plainTextEdit.toPlainText().lower():
            publickey = get_specific_config_interface(
                self.plainTextEdit.toPlainText(), "publickey"
            )
            self.lineEdit.setText(publickey)
