#
#  fletcher_encryption.py
#
#
#  Created by Brandon Fletcher on 8/12/21.
#

from tkinter import *

app = Tk()
app.title("Fletcher Encryption")
app.geometry("900x450")

choose_file_btn = Button(app, text="Choose File")

choose_file_btn.grid(row=0, column=0, rowspan=2)

app.mainloop()
