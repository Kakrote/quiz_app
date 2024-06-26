import customtkinter as ctk
from .utils import rc
from ....lib.struct import ADMIN

class ListItem(ctk.CTkFrame):
    
    namevar:ctk.StringVar=None
    def __init__(self, master, id="DEV", name="", **kwargs):
        super().__init__(master, **kwargs)
        self.configure(height=60)
        self.grid_columnconfigure(0, weight=1)
        # self.grid_propagate(False)
        # transparent
        self.namevar = ctk.StringVar(value=name)
        self.id = id

        self.e_name = ctk.CTkEntry(self, state=ctk.DISABLED, textvariable=self.namevar, fg_color="transparent",font=('sans', 15), border_width=0)
        self.l_id = ctk.CTkLabel(self, text=id, fg_color="transparent", anchor="s", font=('sans', 10), height=15, text_color="#555")
        self.b_edit = ctk.CTkButton(self, text="EDIT", fg_color="green", width=50, command=self.edit_clicked)
        self.b_ban = ctk.CTkButton(self, text="BAN", fg_color="red", width=50)

    def edit_clicked(self):
        if self.e_name.cget("state") == ctk.DISABLED:
            self.e_name.configure(state=ctk.NORMAL, border_width=2)
            self.b_edit.configure(text="SAVE")
            self.e_name.focus()
        else:
            self.e_name.configure(state=ctk.DISABLED, border_width=0)

            name = self.e_name.get()
            clientID = self.id
            admin:ADMIN= ADMIN.me
            admin.setUserData(clientID, name)
            self.b_edit.configure(text="EDIT")

    def show(self, r,c):

        self.e_name.grid(row=0, column=0, sticky="w", padx=20, pady=(5,0))
        self.l_id.grid(row=1, column=0, sticky="w", padx=30, pady=(0,5))
        self.b_edit.grid(row=0, column=1, rowspan=2)
        self.b_ban.grid(row=0, column=2, rowspan=2, padx=(10,20))

        # self.grid(row=r, column=c, sticky="we", padx=5, pady=5)
        self.pack(side=ctk.TOP, fill=ctk.X, padx=5, pady=(5,0))

    def hide(self):
        self.pack_forget()

class List(ctk.CTkFrame):
    items = list()
    def __init__(self, master, **kwargs):
        """attach children and configure grid"""
        super().__init__(master,  **kwargs)
        self.items.append(ListItem(self, name="GROUP-I", fg_color='transparent', border_width=2))
        self.items.append(ListItem(self, name="GROUP-II", fg_color='transparent', border_width=2))
        self.items.append(ListItem(self, name="GROUP-III", fg_color='transparent', border_width=2))
        self.items.append(ListItem(self, name="GROUP-IV", fg_color='transparent', border_width=2))
        self.grid_columnconfigure(0, weight=1)
    
    def update(self):
        for item in self.items:
            item.hide()
        self.items.clear()
        admin:ADMIN = ADMIN.me
        for id, name in zip(admin.participants.getClientIDs(), admin.participants.getNames()):
            self.items.append(ListItem(self,id,name))

    def show(self):
        self.grid(row=1, column=0,sticky="nswe", padx=20)
        for r,item in enumerate(self.items):
            item.show(r=r, c=0)

class ParticipantsFrame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        """attach children and configure grid"""
        super().__init__(master, fg_color="white",  **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.topbar = ctk.CTkLabel(master=self,text="Participants", anchor="w")
        self.list = List(master=self, fg_color="transparent")

    def show(self):
        """render children and current frame"""

        # self.        
        self.list.update()
        self.topbar.configure(text=f"Participants ({len(self.list.items)})")
        self.topbar.grid(row=0, column=0, sticky="we", padx=20, pady=10)

        self.list.show()
        self.grid(row=0, column=0,padx=10, pady=10, sticky="nswe")
