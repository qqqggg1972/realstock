# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'I:\learn\python\realstock\lay.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(231, 164)
        Form.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_head = QtWidgets.QLabel(Form)
        self.label_head.setText("")
        self.label_head.setObjectName("label_head")
        self.horizontalLayout.addWidget(self.label_head)
        self.toolButton_set = QtWidgets.QToolButton(Form)
        self.toolButton_set.setObjectName("toolButton_set")
        self.horizontalLayout.addWidget(self.toolButton_set)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView_stock = QtWidgets.QTableView(Form)
        self.tableView_stock.setShowGrid(False)
        self.tableView_stock.setGridStyle(QtCore.Qt.NoPen)
        self.tableView_stock.setCornerButtonEnabled(False)
        self.tableView_stock.setObjectName("tableView_stock")
        self.verticalLayout.addWidget(self.tableView_stock)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.toolButton_set.setText(_translate("Form", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

