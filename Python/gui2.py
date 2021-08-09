from tkinter import *
from tkinter import StringVar
from tkinter import filedialog
import os

# initializes the GUI, and sets the window size.
app = Tk()
enc_key = StringVar()   # used to store the encryption key
app.geometry("900x450")
app.title("Encryption by Fletcher")

# create the three frames to be used.
left_frame = Frame(app, width=300)
center_frame = Frame(app, width=300)
right_frame = Frame(app, width=300)

left_frame.pack(side = LEFT, expand = YES)
center_frame.pack(side = LEFT, expand = YES)
right_frame.pack(side = LEFT, expand = YES)

# used to give option to choose file.
def get_file_path():
    global file_path
    # Open and return file path
    # file_path= filedialog.askopenfilename(title = "Select A File", filetypes \
    # = (("mov files", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", \
    #"*.avi")))
    file_path= filedialog.askopenfilename(title = "Select A File")

# function used to encrypt the files
def encrypt():
    # openssl enc -aes-256-cbc -in test.txt -out test.txt.enc -pass pass:password
    command = "openssl enc -aes-256-cbc -in " + '"' + file_path + '" ' + "-out \
    " + '"' + file_path + ".enc" + '" ' + "-pass pass:" + '"' + enc_key.get() + '"'
    print(command)
    os.system(command)

# button to choose file to encrypt/decrypt
choose_file_btn = Button(left_frame, text="choose file", command=get_file_path)
choose_file_btn.pack(fill = BOTH)

# have the user input their encryption key
enter_key_label = Label(center_frame, text="enter encryption key:")
enter_key_label.pack(expand = YES)

encryption_key = Entry(center_frame, textvariable=enc_key, show="*", width=27)
encryption_key.pack()

# button to encrypt/decrypt the file
enc_dec_btn = Button(right_frame, text="encrypt", command=encrypt)
enc_dec_btn.pack()

# start the GUI
app.mainloop()
