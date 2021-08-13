#
#  fletcher_encryption.py
#
#
#  Created by Brandon Fletcher on 8/12/21.
#

from tkinter import *

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

# Button used to actually encrypt/decrypt a file.
# TODO: Set the button text to change based off of radio button.
status = IntVar()
status.get()
operation_btn_text = "Encrypt"

radio_btn_frame = Frame(app)
radio_btn_frame.grid(row=0, column=2)

encrypt = Radiobutton(radio_btn_frame, text="Encrypt", variable=status, value=1)
decrypt = Radiobutton(radio_btn_frame, text="Decrypt", variable=status, value=2)

encrypt.pack()
decrypt.pack()


fun_btn = Button(app, text=operation_btn_text)
fun_btn.grid(row=1, column=2, sticky=N)


app.mainloop()
