#
#  app_functions.py
#
#
#  Created by Brandon Fletcher on 8/13/21.
#

from tkinter import filedialog
from tkinter import *
import app_operations

def choose_file():
    global file_path
    file_path= filedialog.askopenfilename(title = "Select A File")


# May need to add to its own module later
# Used to set the text of the button that performs the operation
def op_btn_status(number, button):
    num = number
    operation_btn = button
    if (num == 1):
        operation_btn.configure(text="Encrypt")
        print("This should happen")
    elif (num == 2):
        operation_btn.configure(text="Decrypt")
        print("This didn't happen")
    else:
        operation_btn.configure(text="Encrypt")


# chooses the command to be performed by the button.
# TODO: refactor this to be combined with the above op_btn_status() function.
def operation_btn_cmd(stat, k):
    status = stat
    key = k
    if (status == 1):
        app_operations.encrypt(file_path, key)
    elif (status == 2):
        app_operations.decrypt(file_path, key)
    else:
        app_operations.encrypt(file_path, key)
