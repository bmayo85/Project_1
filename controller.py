from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """
    A class representing the remote control GUI
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Method to set up GUI
        :param args: Allows non-keyword arguments to pass
        :param kwargs: Allows keyword arguments to pass
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_power.clicked.connect(lambda: self.power())
        self.button_mute.clicked.connect(lambda: self.toggle_volume())
        self.dial_channel.valueChanged.connect(lambda: self.monitor())
        self.dial_channel.setDisabled(True)
        self.slider_volume.setDisabled(True)
        self.button_mute.setDisabled(True)

    def power(self) -> None:
        """
        Method to handle power button toggle connection
        """
        if self.dial_channel.isEnabled():
            self.dial_channel.setDisabled(True)
            self.slider_volume.setDisabled(True)
            self.button_mute.setDisabled(True)
            self.display.setPixmap(QtGui.QPixmap("black.jpg"))
        else:
            self.dial_channel.setEnabled(True)
            self.slider_volume.setEnabled(True)
            self.button_mute.setEnabled(True)
            self.monitor()

    def monitor(self) -> None:
        """
        Method to handle monitor display connection
        """
        channel = self.dial_channel.value()
        if channel == 1:
            self.show_news()
        elif channel == 2:
            self.show_animal()
        elif channel == 3:
            self.show_cartoon()

    def toggle_volume(self) -> None:
        """
        Method to handle mute button connection
        """
        if self.slider_volume.isEnabled():
            self.slider_volume.setDisabled(True)
        else:
            self.slider_volume.setEnabled(True)

