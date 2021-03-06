import tkinter
from tkinter import Radiobutton, ttk
from tkinter.filedialog import askopenfilename
from time import sleep
import com
import terminal

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
        self.datei_btn = tkinter.Button(self.bedienung_org_frame, text = "Datei öffnen", width = 12, pady = 2, command=self.open_file)
        self.datei_btn.pack(padx=10)
        #dateiname label
        self.datei_name_label = tkinter.Label(self.bedienung_org_frame, text = ".../code.bas", width=35)
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
        self.progressbar = ttk.Progressbar(self.upload_org_frame, length=200, mode="determinate")
        self.progressbar.pack()
        #upload btn
        self.upload_btn = tkinter.Button(self.upload_org_frame, text = "Upload", width = 12, pady = 2, command=self.upload_cmd)
        self.upload_btn.pack(padx=10)

        self.datei_pfad = ""
        self.code = []
        self.code_len = 0
        self.uploader_state = "idle"
        self.code_pointer = 0

    def open_file(self):
        self.datei_pfad = askopenfilename(filetypes=[("Basic Skript", "*.bas")])
        if self.datei_pfad == "":
            return
        if len(self.datei_pfad) >= 30:
            self.datei_name_label["text"] = "... " + self.datei_pfad[-30:]
        else:
            self.datei_name_label["text"] = self.datei_pfad
    
    def upload_cmd(self):
        if self.uploader_state == "running":
            return
        try:
            file_handler = open(self.datei_pfad)
        except:
            return
        terminal.aktiv = False
        self.code = file_handler.readlines()
        self.code_len = len(self.code)
        self.uploader_state = "running"
        self.code_pointer = 0
        self.progressbar["value"] = 0
        com.println(chr(3))
        sleep(0.3)
        com.println("AUTOSAVE")
    
    def update(self):
        super().update()
        if self.uploader_state == "running":
            #zeile senden
            com.println(self.code[self.code_pointer].replace("\n", "").replace("\r", ""))
            #progressbar
            self.progressbar["value"] = int((self.code_pointer / self.code_len) * 100)
            #pointer inkrementieren
            print(self.code_pointer)
            self.code_pointer += 1
            #wenn alle zeilen gesendet state zu idle setzen
            if self.code_pointer >= self.code_len:
                self.uploader_state = "idle"
                #und stop kondition senden
                sleep(0.3)
                com.println(chr(26))
                self.progressbar["value"] = 100
                com.println("run")
                terminal.aktiv = True
