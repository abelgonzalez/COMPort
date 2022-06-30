# -*- coding: utf-8 -*-
"""
    Visualization module.
    Module with implementations of functions to visualize the streamed information.
"""
import pyqtgraph
import pyqtgraph as pg
from PyQt5 import QtCore
from PyQt5 import QtCore


def setPyQtGraph(pw: pyqtgraph, graphTitle: str, yTitle: str, xTitle: str, maxValue: int, minValue: int, recordTime: int):
    pw.setBackground('w')
    pw.showGrid(x=True, y=True)
    pw.setTitle(graphTitle, color="b", size="15pt")

    styles = {'color': 'r', 'font-size': '15px'}
    pw.setLabel('left', yTitle, **styles)
    pw.setLabel('bottom', xTitle, **styles)

    #x = list(range(1, recordTime+1))
    yMax = [maxValue]*recordTime
    yMin = [minValue]*recordTime

    # Set max value line
    pw.plot(yMax, pen=pg.mkPen('r', width=5))

    # Set min value line
    pw.plot(yMin, pen=pg.mkPen('g', width=5))

    # pg.QtGui.QGuiApplication.exec()

    return pw


def updatePyQtGraph(pw: pyqtgraph, xList: list, yList: list):
    x = xList
    y = yList

    pw.plot(x, y, pen=pg.mkPen(color=(0, 0, 0), width=3, style=QtCore.Qt.SolidLine),
            symbol='o', symbolSize=10, symbolBrush=('b'))

    # pw.plot(x, y, clear= True, pen=pg.mkPen(color=(0, 0, 0), width=3, style=QtCore.Qt.SolidLine),
    #        symbol='o', symbolSize=10, symbolBrush=('b'))

    pg.QtGui.QApplication.processEvents()
