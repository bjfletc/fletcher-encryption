#
#  app_functions.py
#
#
#  Created by Brandon Fletcher on 8/13/21.
#

from tkinter import filedialog

def choose_file():
    global file_path
    file_path= filedialog.askopenfilename(title = "Select A File")
