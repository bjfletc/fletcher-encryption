#
#  app_functions.py
#
#
#  Created by Brandon Fletcher on 8/13/21.
#

from tkinter import filedialog
from tkinter import *

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
