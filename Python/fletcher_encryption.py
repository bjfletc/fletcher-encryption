#
#  fletcher_encryption.py
#
#
#  Created by Brandon Fletcher on 8/12/21.
#

from tkinter import *
from tkinter import StringVar
import app_operations
import app_functions

# Setup and configure the app window.
app = Tk()
app.title("Fletcher Encryption")
app.geometry("900x450")
app.rowconfigure(0, minsize=225)
app.rowconfigure(1, minsize=225)
app.columnconfigure(0, minsize=300)
app.columnconfigure(1, minsize=300)
app.columnconfigure(2, minsize=300)

# Going to allow the user to choose the file to encrypte/decrypt
# with the application.
choose_file_btn = Button(app, text="Choose File", command=app_functions\
.choose_file)
choose_file_btn.grid(row=1, column=0, rowspan=2, sticky=N)

# Where we show the user to enter their encryption key to be able to
# encrypt/decrypt the file of their choosing.
key = StringVar()
key = key.get()

enter_key_lbl = Label(app, text="Enter your encryption key:")
enter_key_lbl.grid(row=0, column=1, sticky=S)

encryption_key = Entry(app, show="*", textvariable=key, width=27)
encryption_key.grid(row=1, column=1, sticky=N)

stat = IntVar()

"""
 This is used to choose the operation the be performed on the file.
 When we choose the encrypt radio button, it will change the operation
 button to encrypt status. Vice versa with choosing decrypt.

 Needed to seperate this into its own frame, so it could occupy the whole
 row in the grid geometry.
"""
radio_btn_frame = Frame(app)
radio_btn_frame.grid(row=0, column=2)

encrypt = Radiobutton(radio_btn_frame, text="Encrypt", variable=stat, value=1\
, command=lambda : app_functions.op_btn_status(stat.get(), operation_btn))
decrypt = Radiobutton(radio_btn_frame, text="Decrypt", variable=stat, value=2\
, command=lambda : app_functions.op_btn_status(stat.get(), operation_btn))

encrypt.pack()
decrypt.pack()

# chooses the command to be performed by the button.
# TODO: refactor this to be combined with the above op_btn_status() function.
def operation_btn_cmd():
    status = stat.get()
    if (status == 1):
        app_operations.encrypt(app_functions.file_path, key)
    elif (status == 2):
        app_operations.decrypt(app_functions.file_path, key)
    else:
        app_operations.encrypt(app_functions.file_path, key)

# Button used to actually encrypt/decrypt a file.
operation_btn = Button(app, text="Encrypt", command=operation_btn_cmd)
operation_btn.grid(row=1, column=2, sticky=N)

app.mainloop()
