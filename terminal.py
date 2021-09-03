import tkinter
from tkinter import ttk
import com
#from befehls_verlauf import BefehlsVerlauf

class Terminal(tkinter.Frame):
    def __init__(self, root, lines_length=100):
        super().__init__(root)
        #org bedienung frame
        self.bedienung_org_frame = tkinter.Frame(root)
        self.bedienung_org_frame.pack(sid = "top")
        #verbinden btn
        self.verbinden_btn = tkinter.Button(self.bedienung_org_frame, text = "Verbinden", width = 12, pady = 2, bg="orange red")
        self.verbinden_btn.grid(column=4, row=0, padx=10)
        #dropdown com
        self.drop_down_com_var = tkinter.StringVar()
        self.drop_down_com = ttk.Combobox(self.bedienung_org_frame, textvariable=self.drop_down_com_var, state="readonly", width=5)
        self.drop_down_com.grid(column=0, row=0)
        #dropdown baud
        self.drop_down_baud_var = tkinter.IntVar()
        self.drop_down_baud = ttk.Combobox(self.bedienung_org_frame, textvariable=self.drop_down_baud_var, state="readonly", width=10)
        self.drop_down_baud["values"] = (110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 57600, 115200, 128000, 256000)
        self.drop_down_baud.current(11)
        self.drop_down_baud.grid(column=1, row=0, padx=20)
        #dropdown terminierung
        self.drop_down_ter_var = tkinter.StringVar()
        self.drop_down_ter = ttk.Combobox(self.bedienung_org_frame, textvariable=self.drop_down_ter_var, state="readonly", width=6)
        self.drop_down_ter["values"] = ("CR", "LF", "CR+LF")
        self.drop_down_ter.current(0)
        self.drop_down_ter.grid(column=2, row=0)
        #autosroll checkbox
        self.autoscroll_checkbox_var = tkinter.IntVar()
        self.autoscroll_checkbox = tkinter.Checkbutton(self.bedienung_org_frame, variable=self.autoscroll_checkbox_var)
        self.autoscroll_checkbox.grid(column=3, row=0, padx=10)
        #srcoll
        self.scroll_org_frame = tkinter.Frame(root)
        self.scroll_org_frame.pack(side = "top")
        self.entry_org_frame = tkinter.Frame(root)
        self.entry_org_frame.pack(side="bottom", pady = 3)
        self.scroll_y = tkinter.Scrollbar(self.scroll_org_frame)
        self.scroll_y.pack(fill = "y", side = "right")
        self.scroll_x = tkinter.Scrollbar(self.scroll_org_frame, orient=tkinter.HORIZONTAL)
        self.scroll_x.pack(side="bottom", fill="x")
        #listbox
        self.listbox = tkinter.Listbox(self.scroll_org_frame, height=30, width=60)
        self.listbox.pack(side="top")
        self.scroll_y["command"] = self.listbox.yview
        self.scroll_x["command"] = self.listbox.xview
        self.listbox["yscrollcommand"] = self.scroll_y.set
        self.listbox["xscrollcommand"] = self.scroll_x.set
        #entry
        self.entry = tkinter.Entry(self.entry_org_frame, width = 63)
        #self.listbox.insert("end", *[i for i in range(100)])
        self.entry.pack()
        #gerbten frame packen
        self.pack()


        #self.verlauf = BefehlsVerlauf(100)

        self.max_length = lines_length
        self.autoscroll = True
        self.verbunden = False
        self.terminierung_lookup = {"CR":"\r", "LF":"\n", "CR+LF":"\r\n"}

        self.drop_down_com["values"] = tuple(map(str, com.get_com_port_list()))

        self.entry.bind('<Return>', self.entry_enter_bind)
        self.entry.bind('<Up>', self.entry_up_bind)
        self.entry.bind('<Down>', self.entry_down_bind)
        self.verbinden_btn["command"] = self.verbinden_cmd


    def autoscroll_on(self):
        self.autoscroll = True

    def autoscroll_off(self):
        self.autoscroll = False

    def entry_enter_bind(self, para):
        pass


    def entry_up_bind(self, para):
        pass

    def entry_down_bind(self, para):
        pass

    def verbinden_cmd(self):
        pass

    def update_com_ports(self):
        pass

    def update(self):
        super().update()