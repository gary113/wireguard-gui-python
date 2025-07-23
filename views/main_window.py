### GENERATED CODE - CLASS ###

from functools import partial

from PyQt6 import QtCore, QtGui, QtWidgets

from utility.functions import *
from utility.log_thread import LogThread
from views.edit_window import Ui_EditWindow
from views.new_window import Ui_NewWindow


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName("MainWindow")
        self.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(900, 600))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton_3 = QtWidgets.QToolButton(self.tab)
        self.toolButton_3.setObjectName("toolButton_3")
        sizePolicy1 = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.toolButton_3.sizePolicy().hasHeightForWidth()
        )
        self.toolButton_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.toolButton_3, 2, 2, 1, 1)

        self.toolButton_2 = QtWidgets.QToolButton(self.tab)
        self.toolButton_2.setObjectName("toolButton_2")
        sizePolicy1.setHeightForWidth(
            self.toolButton_2.sizePolicy().hasHeightForWidth()
        )
        self.toolButton_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.toolButton_2, 2, 1, 1, 1)

        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setObjectName("listWidget")
        sizePolicy2 = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection
        )

        self.gridLayout.addWidget(self.listWidget, 0, 0, 2, 3)

        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.groupBox, 0, 4, 1, 2)

        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.setReadOnly(True)

        self.gridLayout_4.addWidget(self.plainTextEdit_2, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.groupBox_2, 1, 4, 1, 2)

        self.edit_button = QtWidgets.QToolButton(self.tab)
        self.edit_button.setObjectName("toolButton_5")
        self.edit_button.setEnabled(False)
        sizePolicy3 = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.edit_button.sizePolicy().hasHeightForWidth())
        self.edit_button.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.edit_button, 2, 5, 1, 1)

        self.toolButton = QtWidgets.QToolButton(self.tab)
        self.toolButton.setObjectName("toolButton")
        sizePolicy3.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy3)
        self.toolButton.setPopupMode(
            QtWidgets.QToolButton.ToolButtonPopupMode.MenuButtonPopup
        )

        self.gridLayout.addWidget(self.toolButton, 2, 0, 1, 1)

        self.turn_activation_button = QtWidgets.QToolButton(self.tab)
        self.turn_activation_button.setObjectName("toolButton_4")
        self.turn_activation_button.setEnabled(False)
        sizePolicy3.setHeightForWidth(
            self.turn_activation_button.sizePolicy().hasHeightForWidth()
        )
        self.turn_activation_button.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.turn_activation_button, 2, 4, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName("textBrowser")

        self.gridLayout_5.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        ### END GENERATED CODE - CLASS ###

        ### START CUSTOM CODE - CLASS ###

        self.version = "v1.3"

        self.logs_thread = LogThread()
        self.logs_thread.new_log.connect(self.append_log)
        self.logs_thread.start()

        self.setWindowIcon(
            QtGui.QIcon(f"{PROJECT_DIRECTORY}/resources/icons/wireguard-icon.png")
        )

        self.tray_menu = QtWidgets.QMenu()

        tray_interfaces = get_interfaces()
        self.tray_menu_actions_list = []

        if len(tray_interfaces) > 0:
            for i, interface in enumerate(tray_interfaces):
                self.tray_menu_actions_list.append(QtGui.QAction(interface))
                self.tray_menu_actions_list[i].triggered.connect(
                    partial(turn_interface, interface)
                )
                self.tray_menu.addAction(self.tray_menu_actions_list[i])
            self.tray_menu.addSeparator()
            self.update_tray_menu()

        self.tray_menu_show = QtGui.QAction("Show")
        self.tray_menu_show.triggered.connect(self.show_window)
        self.tray_menu_show.setIcon(
            QtGui.QIcon(f"{PROJECT_DIRECTORY}/resources/icons/show-icon.png")
        )

        self.tray_menu_quit = QtGui.QAction("Quit")
        self.tray_menu_quit.triggered.connect(exit)
        self.tray_menu_quit.setIcon(
            QtGui.QIcon(f"{PROJECT_DIRECTORY}/resources/icons/quit-icon.png")
        )

        self.tray_menu.addAction(self.tray_menu_show)
        self.tray_menu.addAction(self.tray_menu_quit)

        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.windowIcon())
        self.tray_icon.activated.connect(self.tray_icon_click)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()

        self.options_menu = QtWidgets.QMenu()

        self.options_menu_import_interfaces = QtGui.QAction("Import interfaces")
        self.options_menu_import_interfaces.triggered.connect(
            self.import_interfaces_option
        )

        self.options_menu_new_interface = QtGui.QAction("New interface")
        self.options_menu_new_interface.triggered.connect(self.new_interface_option)

        self.options_menu.addAction(self.options_menu_new_interface)
        self.options_menu.addAction(self.options_menu_import_interfaces)
        self.toolButton.setMenu(self.options_menu)

        self.listWidget.setDragEnabled(False)
        self.listWidget.addItems(get_interfaces())
        self.listWidget.itemSelectionChanged.connect(self.list_widget_selected)
        self.listWidget.doubleClicked.connect(self.turn_activation_button.click)
        self.update_list()

        self.toolButton.clicked.connect(self.add_interface_button_click)
        self.toolButton_2.clicked.connect(self.delete_button_click)
        self.toolButton_3.clicked.connect(self.export_button_click)
        self.turn_activation_button.clicked.connect(self.activate_button_click)
        self.edit_button.clicked.connect(self.edit_button_click)

        self.toolButton.setIcon(
            QtGui.QIcon(f"{PROJECT_DIRECTORY}/resources/icons/add-icon.png")
        )
        self.toolButton.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon
        )
        self.toolButton_2.setIcon(
            QtGui.QIcon(f"{PROJECT_DIRECTORY}/resources/icons/remove-icon.png")
        )
        self.toolButton_2.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon
        )
        self.toolButton_3.setIcon(
            QtGui.QIcon(f"{PROJECT_DIRECTORY}/resources/icons/zip-icon.png")
        )
        self.toolButton_3.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon
        )
        self.turn_activation_button.setIcon(
            QtGui.QIcon(f"{PROJECT_DIRECTORY}/resources/icons/up-icon.png")
        )
        self.turn_activation_button.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon
        )
        self.edit_button.setIcon(
            QtGui.QIcon(f"{PROJECT_DIRECTORY}/resources/icons/edit-icon.png")
        )
        self.edit_button.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon
        )

        self.statusbar.showMessage(self.version)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_all)
        self.timer.setInterval(UPDATE_INTERVAL)
        self.timer.start()

        ### END CUSTOM CODE - CLASS ###

        ### GENERATED CODE - TRANSLATE ###

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def append_log(self, line):
        self.textBrowser.append(line)

    def retranslateUi(self):
        self.setWindowTitle(
            QtCore.QCoreApplication.translate("MainWindow", "wgp", None)
        )
        self.toolButton_3.setText(
            QtCore.QCoreApplication.translate("MainWindow", "Export", None)
        )
        self.toolButton_2.setText(
            QtCore.QCoreApplication.translate("MainWindow", "Delete", None)
        )
        self.groupBox.setTitle(
            QtCore.QCoreApplication.translate("MainWindow", "Interface", None)
        )
        self.groupBox_2.setTitle(
            QtCore.QCoreApplication.translate("MainWindow", "Peers", None)
        )
        self.edit_button.setText(
            QtCore.QCoreApplication.translate("MainWindow", "Edit", None)
        )
        self.toolButton.setText(
            QtCore.QCoreApplication.translate("MainWindow", "Add interface", None)
        )
        self.turn_activation_button.setText(
            QtCore.QCoreApplication.translate(
                "MainWindow", "Activate / Deactivate", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QtCore.QCoreApplication.translate("MainWindow", "Configs", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QtCore.QCoreApplication.translate("MainWindow", "Logs", None),
        )

    ### END GENERATED CODE - TRANSLATE ###

    ### START CUSTOM CODE - METHODS ###

    # START WIDGETS #

    def list_widget_selected(self):
        if self.listWidget.currentItem() != None:
            self.update_interface_info()
            self.turn_activation_button.setEnabled(True)
            self.edit_button.setEnabled(True)
            self.update_active_button()

    # END WIDGETS #

    # START UPDATES #

    def update_active_button(self):
        current_item = self.listWidget.currentItem()
        if current_item != None:
            current_item = current_item.text()
            if actived_interface(current_item):
                self.turn_activation_button.setText("Deactivate")
                self.turn_activation_button.setIcon(
                    QtGui.QIcon(f"{PROJECT_DIRECTORY}/resources/icons/down-icon.png")
                )
            else:
                self.turn_activation_button.setText("Activate")
                self.turn_activation_button.setIcon(
                    QtGui.QIcon(f"{PROJECT_DIRECTORY}/resources/icons/up-icon.png")
                )

    def update_all(self):
        if self.isActiveWindow():
            if self.tabWidget.currentIndex() == 0:
                self.update_list()
                current_item = self.listWidget.currentItem()
                if current_item != None:
                    self.update_active_button()
                    if actived_interface(current_item.text()):
                        self.update_interface_info()

    def update_list(self):
        interfaces_configs = get_interfaces()
        interfaces_list_witdget = [
            interface.text()
            for interface in self.listWidget.findItems(
                "*", QtCore.Qt.MatchFlag.MatchWildcard
            )
        ]

        for i, interface in enumerate(interfaces_list_witdget):
            if interface not in interfaces_configs:
                self.listWidget.takeItem(i)
                i -= 1

        for i, interface in enumerate(interfaces_configs):
            if interface not in interfaces_list_witdget:
                self.listWidget.insertItem(i, interface)

            if actived_interface(interface):
                self.listWidget.item(i).setIcon(
                    QtGui.QIcon(
                        f"{PROJECT_DIRECTORY}/resources/icons/activated-icon.png"
                    )
                )
            else:
                self.listWidget.item(i).setIcon(
                    QtGui.QIcon(
                        f"{PROJECT_DIRECTORY}/resources/icons/deactivated-icon.png"
                    )
                )

    def update_tray_menu(self):
        interfaces_configs = get_interfaces()
        actions_tray_menu = [action.text() for action in self.tray_menu_actions_list]

        for i, action in enumerate(self.tray_menu_actions_list):
            if action.text() not in interfaces_configs:
                self.tray_menu_actions_list.remove(action)
                i -= 1

        for i, interface in enumerate(interfaces_configs):
            if interface not in actions_tray_menu:
                self.tray_menu_actions_list.insert(i, QtGui.QAction(interface))
                self.tray_menu_actions_list[i].triggered.connect(
                    partial(turn_interface, interface)
                )
                self.tray_menu.insertAction(
                    self.tray_menu.actions()[i], self.tray_menu_actions_list[i]
                )
                self.tray_menu.insertSeparator(self.tray_menu.actions()[-2])

            if actived_interface(interface):
                self.tray_menu_actions_list[i].setIcon(
                    QtGui.QIcon(
                        f"{PROJECT_DIRECTORY}/resources/icons/activated-icon.png"
                    )
                )
            else:
                self.tray_menu_actions_list[i].setIcon(
                    QtGui.QIcon(
                        f"{PROJECT_DIRECTORY}/resources/icons/deactivated-icon.png"
                    )
                )

    def update_interface_info(self):
        current_item = self.listWidget.currentItem()
        if current_item != None:
            current_item = current_item.text()
            actived = actived_interface(current_item)

            self.groupBox.setTitle(f"Interface: {get_interface_name(current_item)}")

            if actived:
                full_interface_config = get_config_active_content(current_item)
                interface_config = full_interface_config["interface_content"]
                peers_config = full_interface_config["peers_content"]
            else:
                full_interface_config = get_config_file_content(current_item)
                interface_config = full_interface_config["interface_content"]
                peers_config = full_interface_config["peers_content"]

            self.plainTextEdit.setPlainText(interface_config)
            self.plainTextEdit_2.setPlainText(peers_config)

    # END UPDATES #

    # START EVENTS #

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Escape:
            self.listWidget.clearSelection()

    def closeEvent(self, event):
        self.logs_thread.stop()
        self.logs_thread.wait()

        event.accept()

        # event.ignore()
        # self.hide()

    # END EVENTS #

    # START BUTTONS #

    def activate_button_click(self):
        current_item = self.listWidget.currentItem()

        if current_item != None:
            current_item = current_item.text()
            turn_interface(current_item)

            self.update_active_button()
            self.update_interface_info()
            self.update_list()
        else:
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Error",
                "You have to select an interface",
            ).exec()

    def edit_button_click(self):
        current_item = self.listWidget.currentItem()

        if current_item != None:
            current_item = current_item.text()
            edit_window = Ui_EditWindow(current_item)
            old_config = get_config_file_content(current_item)["full_content"]

            if edit_window.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                new_name = edit_window.lineEdit_2.text()
                new_config = edit_window.plainTextEdit.toPlainText()
                if edit_interface(current_item, new_name, old_config, new_config):
                    if new_name != get_interface_name(current_item):
                        self.update_list()
                    if new_config != old_config:
                        self.update_interface_info()
                    QtWidgets.QMessageBox(
                        QtWidgets.QMessageBox.Icon.Information,
                        "Success",
                        "Configuration updated successfully",
                    ).exec()
                else:
                    QtWidgets.QMessageBox(
                        QtWidgets.QMessageBox.Icon.Critical,
                        "Error",
                        "Invalid configuration, returning to the previous configuration",
                    ).exec()
        else:
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Error",
                "You have to select an interface",
            ).exec()

    def delete_button_click(self):
        selected_items = self.listWidget.selectedItems()
        if selected_items:
            reply = QtWidgets.QMessageBox.question(
                self,
                "Confirm deleting",
                f"Are you sure you want to delete {len(selected_items)} interfaces?",
                QtWidgets.QMessageBox.StandardButton.Yes
                | QtWidgets.QMessageBox.StandardButton.No,
                QtWidgets.QMessageBox.StandardButton.No,
            )
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                for item in selected_items:
                    self.listWidget.takeItem(self.listWidget.row(item))
                    delete_interface(item.text())

                if self.listWidget.count() == 0:
                    self.plainTextEdit.clear()
                    self.plainTextEdit_2.clear()
                    self.turn_activation_button.setText("Activate / Deactivate")
                    self.turn_activation_button.setEnabled(False)
                    self.edit_button.setEnabled(False)
        else:
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Error",
                "You have to select an interface",
            ).exec()

    def export_button_click(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select directory")
        if directory != "" and export_interfaces(directory):
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Information,
                "Success",
                "Interfaces exported successfully",
            ).exec()

    def add_interface_button_click(self):
        interface_file = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select config file", filter="*.conf"
        )[0]
        if interface_file != "" and add_interface(interface_file):
            self.update_list()
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Information,
                "Success",
                "Interface added successfully",
            ).exec()

    # END BUTTONS #

    # START OPTIONS #

    def import_interfaces_option(self):
        interfaces_zip_file = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select zip file", filter="*.zip"
        )[0]
        if interfaces_zip_file != "" and import_interfaces(interfaces_zip_file):
            self.update_list()
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Information,
                "Success",
                "Interfaces imported successfully",
            ).exec()

    def new_interface_option(self):
        new_window = Ui_NewWindow()

        if new_window.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            interface_name = new_window.lineEdit.text()
            interface_config = new_window.plainTextEdit.toPlainText()
            if (
                interface_name.strip() != ""
                and interface_config.strip() != ""
                and new_interface(interface_name, interface_config)
            ):
                self.update_list()
                QtWidgets.QMessageBox(
                    QtWidgets.QMessageBox.Icon.Information,
                    "Success",
                    f"Interface {interface_name} added successfully",
                ).exec()
            else:
                QtWidgets.QMessageBox(
                    QtWidgets.QMessageBox.Icon.Critical,
                    "Error",
                    "Invalid configuration, interface didn't created",
                ).exec()

    # END OPTIONS #

    # START TRAY ICON #

    def tray_icon_click(self):
        self.update_tray_menu()
        menu = self.tray_icon.contextMenu()
        menu.popup(self.tray_icon.geometry().center())

    def show_window(self):
        self.show()
        self.setWindowState(QtCore.Qt.WindowState.WindowNoState)

    # END TRAY ICON #


### END CUSTOM CODE - METHODS ###
