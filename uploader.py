import tkinter
from tkinter import Radiobutton, ttk
import com

class Uploader(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        #upload frame
        self.upload_org_frame = tkinter.Frame(root)
        self.upload_org_frame.pack(side = "bottom")
        #bedings frame
        self.bedienung_org_frame = tkinter.Frame(root)
        self.bedienung_org_frame.pack(side = "top")
        #datei auswählen btn
        self.verbinden_btn = tkinter.Button(self.bedienung_org_frame, text = "Datei öffnen", width = 12, pady = 2)
        self.verbinden_btn.pack(padx=10)
        #dateiname label
        self.datei_name_label = tkinter.Label(self.bedienung_org_frame, text = ".../code.bas")
        self.datei_name_label.pack()
        #radio buttons crunch
        self.crunch = tkinter.IntVar()
        self.crunch_radiobtn_kein_crunch = tkinter.Radiobutton(self.bedienung_org_frame, text="kein Crunch", variable=self.crunch, value=0)
        self.crunch_radiobtn_kein_crunch.pack()
        self.crunch_radiobtn_crunch = tkinter.Radiobutton(self.bedienung_org_frame, text="Crunch", variable=self.crunch, value=1)
        self.crunch_radiobtn_crunch.pack()
        self.crunch_radiobtn_super_crunch = tkinter.Radiobutton(self.bedienung_org_frame, text="super Crunch", variable=self.crunch, value=2)
        self.crunch_radiobtn_super_crunch.pack()
        #progressbar
        self.progressbar = ttk.Progressbar(self.upload_org_frame, length=100, mode="indeterminate")
        self.progressbar.pack()
        #upload btn
        self.upload_btn = tkinter.Button(self.upload_org_frame, text = "Upload", width = 12, pady = 2)
        self.upload_btn.pack(padx=10)