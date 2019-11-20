#!/usr/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.label = Gtk.Label(label="Hey brother!", angle=25, halign=Gtk.Align.END)
        self.add(self.label)

        # See all props of widget
        print(dir(self.label.props))

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()