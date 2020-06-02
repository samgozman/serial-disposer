# -*- coding: utf-8 -*-
# !/usr/bin/env python3.7
import sys
from PyQt5 import QtWidgets
from ui import ui


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ui.SerialDisposerApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

