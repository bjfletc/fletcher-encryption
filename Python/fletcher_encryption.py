#
#  fletcher_encryption.py
#
#
#  Created by Brandon Fletcher on 8/12/21.
#

from tkinter import *

# May need to add to its own module later
# Used to set the text of the button that performs the operation
def op_btn_status():
    num = status.get()
    if (num == 1):
        operation_btn.configure(text="Encrypt")
        print("This should happen")
    elif (num == 2):
        operation_btn.configure(text="Decrypt")
        print("This didn't happen")
    else:
        operation_btn.configure(text="Encrypt")


# Setup and configure the app window.
app = Tk()
app.title("Fletcher Encryption")
app.geometry("900x450")
app.rowconfigure(0, minsize=225)
app.rowconfigure(1, minsize=225)
app.columnconfigure(0, minsize=300)
app.columnconfigure(1, minsize=300)
app.columnconfigure(2, minsize=300)

# Going to allow the user to choose the file to encrypte/decrypte
# with the application.
# TODO: Implement choosing the file command.
choose_file_btn = Button(app, text="Choose File")
choose_file_btn.grid(row=1, column=0, rowspan=2, sticky=N)

# Where we show the user to enter their encryption key to be able to
# encrypt/decrypt the file of their choosing.
enter_key_lbl = Label(app, text="Enter your encryption key:")
enter_key_lbl.grid(row=0, column=1, sticky=S)

encryption_key = Entry(app, show="*", width=27)
encryption_key.grid(row=1, column=1, sticky=N)

status = IntVar()
status.get()

"""
 This is used to choose the operation the be performed on the file.
 When we choose the encrypt radio button, it will change the operation
 button to encrypt status. Vice versa with choosing decrypt.

 Needed to seperate this into its own frame, so it could occupy the whole
 row in the grid geometry.
"""
radio_btn_frame = Frame(app)
radio_btn_frame.grid(row=0, column=2)

encrypt = Radiobutton(radio_btn_frame, text="Encrypt", variable=status, value=1\
, command=fun_btn_status)
decrypt = Radiobutton(radio_btn_frame, text="Decrypt", variable=status, value=2\
, command=fun_btn_status)

encrypt.pack()
decrypt.pack()


# Button used to actually encrypt/decrypt a file.
operation_btn = Button(app, text="Encrypt")
operation_btn.grid(row=1, column=2, sticky=N)

app.mainloop()
