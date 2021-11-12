import sys
from des import *
import sqlite3
from PyQt5.QtWidgets import QMainWindow
from player import Ui_MainWindow
from PyQt5 import QtMultimedia
from add_tracks_form import *
import os

path = 'tracks'
files = os.listdir(path)

con = sqlite3.connect('users')
cur = con.cursor()

for el in files:
    try:
        cur.execute(f"INSERT INTO tracks(track) VALUES('{el}')")
    except:
        continue

con.commit()
cur.close()
con.close()


class AddTracksForm(QMainWindow, Ui_Change_Form):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.player = QtMultimedia.QMediaPlayer()
        con = sqlite3.connect('users')
        cur = con.cursor()
        # Проверяем есть ли такой пользователь
        cur.execute(f'SELECT * FROM tracks')
        value = cur.fetchall()
        self.lst = [el[1] for el in value]
        for el in self.lst:
            self.listWidget.addItem(el)
        self.listWidget.currentItemChanged.connect(self.item)
        self.close_button.clicked.connect(self.close)
        self.addtrack_button.clicked.connect(self.add_track)

    def closeEvent(self, event):
        self.player.stop()
        event.accept()

    def item(self, arg=None):
        self.song = arg.text()
        self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(f'tracks/{self.song}')))
        self.player.play()

    def close(self):
        self.player.stop()
        self.hide()

    def add_track(self):
        con = sqlite3.connect('users')
        cur = con.cursor()
        cur.execute(f'SELECT id FROM users WHERE name="{name}";')
        id_user = cur.fetchall()[0][0]
        cur.execute(f'SELECT id FROM tracks WHERE track="{self.song}";')
        id_track = cur.fetchall()[0][0]
        cur.execute(f"INSERT INTO favorites(user_id, track_id) VALUES({id_user}, {id_track})")
        con.commit()
        QtWidgets.QMessageBox.about(self, 'Оповещение', 'Трек успешно добавлен!')


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.ad = AddTracksForm()
        self.player = QtMultimedia.QMediaPlayer()
        self.listWidget.currentItemChanged.connect(self.item)
        self.play_button.clicked.connect(self.play)
        self.pause_button.clicked.connect(self.pause)
        self.player.stateChanged.connect(self.player_state)
        self.horizontalSlider.sliderMoved[int].connect(self.set_play_position)
        self.horizontalSlider.sliderReleased.connect(self.slider_released)
        self.horizontalSlider.setEnabled(False)
        self.play_repeat = True
        self.play_pause = True
        self.volume = 50
        self.player.setVolume(self.volume)
        self.next_button.clicked.connect(self.next)
        self.previos_button.clicked.connect(self.previos)
        self.repeat_button.clicked.connect(self.repeat)
        self.valuemin_button.clicked.connect(self.volumemin)
        self.valuemax_button.clicked.connect(self.volumemax)
        self.add_button.clicked.connect(self.add_track)
        self.dell_button.clicked.connect(self.dell_track)
        self.change_user_button.clicked.connect(self.change_user)
        self.renew_button.clicked.connect(self.refresh)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.play_mode)
        self.timer.start(1000)

    def refresh(self):
        con = sqlite3.connect('users')
        cur = con.cursor()
        cur.execute(f'SELECT id FROM users WHERE name="{name}";')
        id_user = cur.fetchall()[0][0]
        cur.execute(f'SELECT track_id FROM favorites WHERE user_id="{id_user}";')
        value = cur.fetchall()
        self.lst = []
        self.tracks = []
        for el in value:
            cur.execute(f'SELECT track FROM tracks WHERE id="{el[0]}";')
            self.tracks.append(cur.fetchall()[0][0])
        self.result = []
        for el in self.tracks:
            if el in self.result:
                continue
            else:
                self.result.append(el)
        items = []
        for x in range(self.listWidget.count()):
            items.append(self.listWidget.item(x).text())
        for el in self.result:
            if el not in items:
                self.listWidget.addItem(el)
        if len(items) > 1:
            for el in items:
                if el not in self.result:
                    self.listWidget.takeItem(items.index(el))

    def change_user(self):
        self.close()
        mywin.show()

    def dell_track(self):
        if len(self.result) > 1:
            con = sqlite3.connect('users')
            cur = con.cursor()
            cur.execute(f'SELECT id FROM tracks WHERE track="{self.song}";')
            id_track = cur.fetchall()[0][0]
            cur.execute(f'DELETE FROM favorites WHERE track_id = {id_track}')
            con.commit()
            QtWidgets.QMessageBox.about(self, 'Оповещение', 'Трек успешно удалён!')
            self.refresh()
        else:
            QtWidgets.QMessageBox.about(self, 'Оповещение', 'В плейлисте должен быть хотябы один трек!')

    def add_track(self):
        self.ad.show()

    def volumemin(self):
        self.volume -= 10
        self.player.setVolume(self.volume)

    def volumemax(self):
        self.volume += 10
        self.player.setVolume(self.volume)

    def next(self):
        if len(self.result) > 1:
            if self.result.index(self.song) == len(self.result) - 1:
                self.song = self.result[0]
            else:
                self.song = self.result[self.result.index(self.song) + 1]
        self.listWidget.setCurrentRow(self.result.index(self.song))

    def previos(self):
        if len(self.result) > 1:
            if self.result.index(self.song) == 0:
                self.song = self.result[-1]
            else:
                self.song = self.result[self.result.index(self.song) - 1]
        self.listWidget.setCurrentRow(self.result.index(self.song))

    def item(self, arg=None):
        self.song = arg.text()

    def play_mode(self):
        if self.play_pause == False:
            self.horizontalSlider.setMinimum(0)
            self.horizontalSlider.setMaximum(self.player.duration())
            self.horizontalSlider.setValue(self.horizontalSlider.value() + 1000)

    def slider_released(self):
        self.player.setPosition(self.horizontalSlider.value())

    def set_play_position(self, val):
        pass

    def play(self):
        self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(f'tracks/{self.song}')))
        self.player.play()
        self.play_pause = False
        self.horizontalSlider.setEnabled(True)

    def pause(self):
        self.player.pause()
        self.play_pause = True

    def player_state(self, state):
        if state == 0:
            self.play_pause = True  # -Play_Pause / + play_pause
            self.horizontalSlider.setSliderPosition(0)
            self.horizontalSlider.setEnabled(False)
            if self.play_repeat == True:
                self.play_pause = False  # -Play_Pause / + play_pause

                ###                self.play(self.song)                    # ---
                self.player.play()  # +++

    def repeat(self):
        if self.play_repeat == False:
            self.play_repeat = True
        else:
            self.play_repeat = False


class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.reg)
        self.ui.pushButton_2.clicked.connect(self.auth)
        self.ex = MyWidget()

    def auth(self):
        global name
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        con = sqlite3.connect('users')
        cur = con.cursor()

        # Проверяем есть ли такой пользователь
        cur.execute(f'SELECT * FROM users WHERE name="{name}";')
        value = cur.fetchall()

        if value != [] and value[0][2] == passw:
            QtWidgets.QMessageBox.about(self, 'Оповещение', 'Успешная авторизация!')
            mywin.close()
            self.ex.show()
            self.ex.refresh()
        else:
            QtWidgets.QMessageBox.about(self, 'Оповещение', 'Проверьте правильность ввода данных!')

        cur.close()
        con.close()

    def reg(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        con = sqlite3.connect('users')
        cur = con.cursor()

        cur.execute(f'SELECT * FROM users WHERE name="{name}";')
        value = cur.fetchall()

        if value != []:
            QtWidgets.QMessageBox.about(self, 'Оповещение', 'Такой ник уже используется!')
        elif value == []:
            cur.execute(f"INSERT INTO users (name, password) VALUES ('{name}', '{passw}')")
            QtWidgets.QMessageBox.about(self, 'Оповещение', 'Вы успешно зарегистрированы!')
            con.commit()

        cur.close()
        con.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icons/icon.png'))
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())
