# -*- coding: utf-8 -*-

"""
Module implementing lay.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_lay import Ui_Form
import json
import operator


class lay(QtWidgets.QWidget, Ui_Form):
    """
    Class documentation goes here.
    """

    def __init__(self, data, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(lay, self).__init__(parent)
        self.setupUi(self)

        self.model = QtGui.QStandardItemModel(len(data), 3)

        for row in range(len(data)):
            item = QtGui.QStandardItem(data[row]['zjm']+data[row]['code'])
            self.model.setItem(row, 0, item)

        self.tableView_stock.setModel(self.model)


        #    QtWidgets.QMessageBox.information(self, "Error", str(e))

    @pyqtSlot()
    def on_toolButton_set_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        pass

    @pyqtSlot(QtCore.QModelIndex)
    def on_tableView_stock_clicked(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        pass


if __name__ == '__main__':
    # 获取数据
    json_data = open("set.json").read()
    data = json.loads(json_data)['stock']

    import sys

    app = QtWidgets.QApplication(sys.argv)
    dlg = lay(data)
    dlg.show()

    my_array = [['0', 1, 3.3],
                ['1', 3, 4.5],
                ['5', 7, 2.33]]

    # tablemodel = MyTableModel(my_array, self)

    # Ui_Form.tableview.setModel(tablemodel)

    sys.exit(app.exec_())
