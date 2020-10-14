import sys, data, re, yaml
from PyQt5 import uic, QtCore, QtGui, QtWidgets

class Settings(QtWidgets.QMainWindow):
    """window for settings"""
    def __init__(self, *args, parent=None, **kwargs):
        super(Settings, self).__init__(*args, parent, **kwargs)
        settings = uic.loadUi("ui/settings.ui", self)
        self.actionVerlassen.triggered.connect(self.close)
        self.b_cancel.clicked.connect(self.close)
        self.b_ok.clicked.connect(self.ok)
        self.b_save.clicked.connect(self.save) # "Übernehmen" button
        try:
            with open("settings.yml", "r") as f:
                conf = yaml.load(f, Loader=yaml.FullLoader)
                self.canvas_width.setValue(conf["canvas"]["width"])
                self.canvas_height.setValue(conf["canvas"]["height"])
                self.do_restart.setChecked(bool(int(conf["do_restart"])))
                self.do_testing.setChecked(bool(int(conf["do_testing"])))
                self.color_objects_r.setValue(conf["color"]["objects"]["r"])
                self.color_objects_g.setValue(conf["color"]["objects"]["g"])
                self.color_objects_g.setValue(conf["color"]["objects"]["g"])
                self.color_pointer_r.setValue(conf["color"]["pointer"]["r"])
                self.color_pointer_g.setValue(conf["color"]["pointer"]["g"])
                self.color_pointer_b.setValue(conf["color"]["pointer"]["b"])
                self.update_rate.setValue(conf["update_rate"])
                self.max_seconds.setValue(conf["max_seconds"])
                self.t_factor.setValue(conf["t_factor"])
        except FileNotFoundError:
            with open("settings.yml", "w+") as f:
                f.write("")

    def save(self):
        with open("settings.yml", "w+") as f:
            conf = {
            "canvas": {"width": self.canvas_width.value(), "height": self.canvas_height.value()},
            "do_restart": int(self.do_restart.isChecked()),
            "do_testing": int(self.do_testing.isChecked()),
            "color": {
            "objects": {"r": self.color_objects_r.value(), "g": self.color_objects_g.value(), "b": self.color_objects_b.value()},
            "pointer": {"r": self.color_pointer_r.value(), "g": self.color_pointer_g.value(), "b": self.color_pointer_b.value()}
            },
            "update_rate": self.update_rate.value(),
            "max_seconds": self.max_seconds.value(),
            "t_factor": self.t_factor.value()
            }
            f.write(yaml.dump(conf))

    def ok(self):
        self.save()
        self.close()
