import sys
import pandas as pd
from PyQt5 import uic, QtGui, QtWidgets, QtCore
import asyncio
import time
from app import Api

from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('template.ui', self)         # ./venv/lib/python3.8/site-packages/qt5_applications/Qt/bin/designer &
        self.initUI()
        self.btnCalculateSignal.clicked.connect(self._getPageByUrl)

    def initUI(self):
        self.actionAbout.triggered.connect(self._actionAbout)

        self.actionQuit.setShortcut('Ctrl+Q')
        self.actionQuit.setStatusTip('Exit application')
        self.actionQuit.triggered.connect(QtWidgets.qApp.quit)

    def _actionAbout(self):
        mbox = QtWidgets.QMessageBox(self.menuHelp)
        mbox.setText('Signal generator')
        mbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mbox.setDefaultButton(QtWidgets.QMessageBox.Ok)
        mbox.setIcon(QtWidgets.QMessageBox.Information)
        mbox.setWindowTitle('About')
        mbox.exec()

    async def do_after_sleep(self, period=1, ):
        await asyncio.sleep(period)
        self.resText = ''

    def _getPageByUrl(self):
        url = self.urlLineEdit.text()
        signalType = self.signalTypeComboBox.currentText()
        exportFormat = self.exportFormatComboBox.currentText()
        # print(signalType, exportFormat)
        # print(url)
        if url:
            api = Api(url)
            api._get_page()
            api._get_int_signal()
            if api.page:
                self.resText = 'Done'
                self.currentSignal = getattr(api, signalType)
                self.currentExportFormat = api.exportFormat.get(exportFormat)
                # print(self.currentSignal[:10], self.currentExportFormat)

                if not hasattr(self, 'toolbar'):
                    layout = QtWidgets.QVBoxLayout(self.graphicsView)
                    static_canvas = FigureCanvas(Figure(figsize=(15, 7)))
                    layout.addWidget(static_canvas)
                    self.toolbar = NavigationToolbar(static_canvas, self)
                    self.addToolBar(self.toolbar)

                    self._static_ax = static_canvas.figure.subplots()
                    series = pd.Series(self.currentSignal)
                    self._static_ax.plot(series.index, self.currentSignal)


                # dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
                # layout.addWidget(dynamic_canvas)
                # self.addToolBar(QtCore.Qt.BottomToolBarArea,
                #                 NavigationToolbar(dynamic_canvas, self))

                # self._dynamic_ax = dynamic_canvas.figure.subplots()
                # t = np.linspace(0, 10, 101)
                # # Set up a Line2D.
                # self._line, = self._dynamic_ax.plot(t, np.sin(t + time.time()))
                # self._timer = dynamic_canvas.new_timer(50)
                # self._timer.add_callback(self._update_canvas)
                # self._timer.start()
                else:
                    self._static_ax.clear()
                    series = pd.Series(self.currentSignal)
                    self._static_ax.plot(series.index, self.currentSignal)
                    self._static_ax.figure.canvas.draw()
            else:
                self.resText = 'Error. Check an Url'

            self.actionResultabel.setText(self.resText)
            thread = DummyThread(self)
            thread.start()
            thread.finished.connect(lambda txt='', lbl=self.actionResultabel: lbl.setText(""))

    # def _update_canvas(self):
    #     t = np.linspace(0, 10, 101)
    #     # Shift the sinusoid as a function of time.
    #     self._line.set_data(t, np.sin(t + time.time()))
    #     self._line.figure.canvas.draw()


class DummyThread(QtCore.QThread):
    finished = QtCore.pyqtSignal()

    def run(self):
        time.sleep(1)
        self.finished.emit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())
