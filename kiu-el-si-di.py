# Kiu-El-Si-Di main script
# Copyright (C) 2022 Erdem Ersoy (eersoy93)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
from PyQt6.QtCore import QTimer, QTime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLCDNumber

class KiuElSiDi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.qlcd = QLCDNumber(self)
        self.qlcd.setSegmentStyle(QLCDNumber.SegmentStyle.Flat),

        self.setCentralWidget(self.qlcd)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

        self.showTime()

        self.center()
        self.setFixedSize(300, 150)
        self.setWindowTitle("Kiu-El-Si-Di")
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showTime(self):
        time = QTime.currentTime()
        timeText = time.toString("hh:mm")
        if (time.second() % 2) == 0:
            timeText = timeText.replace(":", " ", 1)

        self.qlcd.display(timeText)

def main(args):
    app = QApplication(args)
    kiuelsidi = KiuElSiDi()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
