'''
Created on 23.06.2020
@author: flori
'''

import sys, data, examples, settings
import vpython as vp
from PyQt5 import uic, QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    """the main window, or entry window"""
    def __init__(self, *args, parent = None, **kwargs):
        super(MainWindow, self).__init__(*args, parent, **kwargs)
        uic.loadUi("entry.ui", self)
        self.setWindowIcon(QtGui.QIcon("icon.gif"))
        self.examples = examples.Examples(parent = self)
        self.settings = settings.Settings(parent = self)
        self.b_ok.clicked.connect(self.open_vpython)
        self.b_reset.clicked.connect(self.clear_fields)
        self.actionListe_mit_Voreinstellungen.triggered.connect(self.examples.show)
        self.actionVerlassen.triggered.connect(app.exit)
        self.actionEinstellungen.triggered.connect(self.settings.show)

    def read(self):
        """make all the entered values globally accessible"""
        global central_mass
        central_mass = float(self.central_mass.text())
        global central_radius
        central_radius = float(self.central_radius.text())
        global sat_mass
        sat_mass = float(self.sat_mass.text())
        global sat_radius
        sat_radius = float(self.sat_radius.text())
        global distance
        distance = float(self.distance.text()) + central_radius + sat_radius

    def clear_fields(self):
        """delete all values in all fields"""
        self.central_radius.setText("")
        self.central_mass.setText("")
        self.sat_mass.setText("")
        self.sat_radius.setText("")
        self.distance.setText("")

    def open_vpython(self):
        """open vpython window with entered values"""
        self.read()
        central = vp.sphere(radius = central_radius)
        sat = vp.sphere(pos = vp.vector(distance,0,0), radius = sat_radius, make_trail = True)
        central_pointer = vp.arrow(axis = vp.vector(0,-(distance / 5),0), color = vp.vector(1,0,0)) # set pointer arrows to the objects because the scales are too large
        central_pointer.pos = central.pos - central_pointer.axis
        sat_pointer = vp.arrow(axis = vp.vector(0,-(distance / 5),0), color = vp.vector(1,0,0))
        sat_pointer.pos = sat.pos - sat_pointer.axis
        x = 0
        while x < 300: # simple movement
            vp.rate(30)
            sat.pos += vp.vector(distance,0,0) / 300
            sat_pointer.pos = sat.pos - sat_pointer.axis
            x += 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
