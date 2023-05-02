from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """
    A class representing the remote control GUI
    """
    # List for dial entry created outside of methods to function properly
    prev_dial = ['None']

    def __init__(self, *args, **kwargs) -> None:
        """
        Method to set up GUI
        :param args: Allows non-keyword arguments to pass
        :param kwargs: Allows keyword arguments to pass
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.push_status.clicked.connect(lambda: self.status())
        self.radio_0.setDisabled(True)
        self.radio_10.setDisabled(True)
        self.radio_20.setDisabled(True)
        self.radio_30.setDisabled(True)
        self.radio_40.setDisabled(True)
        self.radio_50.setDisabled(True)
        self.radio_60.setDisabled(True)
        self.radio_70.setDisabled(True)
        self.radio_80.setDisabled(True)
        self.radio_90.setDisabled(True)
        self.radio_100.setDisabled(True)
        self.check_mute.setDisabled(True)
        self.dial_channel.setDisabled(True)
        self.entry_bookmark.setDisabled(True)

    def status(self) -> None:
        """
        Method that handles status prompt in GUI when clicked.
        :return: TV Status when exception is triggered, otherwise return invalid entry message to user.
        """
        power = self.slider_power.value()
        channel = self.dial_channel.value()
        bookmark = self.entry_bookmark.text()
        self.radio_0.setDisabled(True)
        self.radio_10.setDisabled(True)
        self.radio_20.setDisabled(True)
        self.radio_30.setDisabled(True)
        self.radio_40.setDisabled(True)
        self.radio_50.setDisabled(True)
        self.radio_60.setDisabled(True)
        self.radio_70.setDisabled(True)
        self.radio_80.setDisabled(True)
        self.radio_90.setDisabled(True)
        self.radio_100.setDisabled(True)
        self.check_mute.setDisabled(True)
        self.dial_channel.setDisabled(True)
        self.entry_bookmark.setDisabled(True)
        dial = 'None'

        if self.check_mute.isChecked():
            volume = 0
        elif self.radio_0.isChecked():
            volume = 0
        elif self.radio_10.isChecked():
            volume = 10
        elif self.radio_20.isChecked():
            volume = 20
        elif self.radio_30.isChecked():
            volume = 30
        elif self.radio_40.isChecked():
            volume = 40
        elif self.radio_50.isChecked():
            volume = 50
        elif self.radio_60.isChecked():
            volume = 60
        elif self.radio_70.isChecked():
            volume = 70
        elif self.radio_80.isChecked():
            volume = 80
        elif self.radio_90.isChecked():
            volume = 90
        elif self.radio_100.isChecked():
            volume = 100

        if power == 1:
            self.entry_bookmark.setDisabled(False)
            self.radio_0.setDisabled(False)
            self.radio_10.setDisabled(False)
            self.radio_20.setDisabled(False)
            self.radio_30.setDisabled(False)
            self.radio_40.setDisabled(False)
            self.radio_50.setDisabled(False)
            self.radio_60.setDisabled(False)
            self.radio_70.setDisabled(False)
            self.radio_80.setDisabled(False)
            self.radio_90.setDisabled(False)
            self.radio_100.setDisabled(False)
            self.check_mute.setDisabled(False)
            self.dial_channel.setDisabled(False)
            if type(bookmark) == str:
                try:
                    float(bookmark)
                    self.label_bookmark_prompt.setText('Enter valid answer (Y/N)')
                except ValueError:
                    bookmark = self.entry_bookmark.text().upper().strip()
                    if bookmark == 'Y' or bookmark == 'N':
                        self.entry_bookmark.clear()
                        if bookmark == 'Y':
                            dial = self.dial_channel.value()
                            self.prev_dial.append(dial)
                            self.label_bookmark_prompt.setText(f'Channel {channel} successfully saved')
                        elif bookmark == 'N':
                            self.label_bookmark_prompt.clear()
                            if self.prev_dial:
                                dial = self.prev_dial[-1]
                        self.label_status.setText(f'Power: ON\nVolume: {volume}\nChannel: {channel}\nBookmark: {dial}')

                    else:
                        if bookmark != '':
                            self.label_bookmark_prompt.setText('Enter valid answer (Y/N)')

        else:
            self.entry_bookmark.setDisabled(True)
            self.entry_bookmark.clear()
            self.label_bookmark_prompt.clear()
            self.label_status.clear()
            self.radio_0.setDisabled(True)
            self.radio_10.setDisabled(True)
            self.radio_20.setDisabled(True)
            self.radio_30.setDisabled(True)
            self.radio_40.setDisabled(True)
            self.radio_50.setDisabled(True)
            self.radio_60.setDisabled(True)
            self.radio_70.setDisabled(True)
            self.radio_80.setDisabled(True)
            self.radio_90.setDisabled(True)
            self.radio_100.setDisabled(True)
            self.check_mute.setDisabled(True)
            self.dial_channel.setDisabled(True)
