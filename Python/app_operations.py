#
#  app_operations.py
#
#
#  Created by Brandon Fletcher on 8/12/21.
#

import os   # needed to access openssl
from tkinter import *   # for getting the file

def encrypt(file_path, encryption_key):
    openssl_cmd = "openssl enc -aes-256-cbc -in " + '"' + file_path + '" ' + \
    "-out " + '"' + file_path + ".enc" + '" ' + "-pass pass:" + '"' + \
    encryption_key + '"'
    print("encrypt")
    os.system(openssl_cmd)


def decrypt(file_path, decryption_key):
    file = file_path[:file_path.find(".enc")]
    openssl_cmd = "openssl enc -aes-256-cbc -in " + '"' + file_path + '" ' + \
    "-out " + '"' + file + '" -d ' + "-pass pass:" + '"' + decryption_key + '"'
    print("decrypt")
    os.system(openssl_cmd)

# used to give option to choose file.
def get_file_path():
    global file_path
    # Open and return file path
    # file_path= filedialog.askopenfilename(title = "Select A File", filetypes \
    # = (("mov files", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", \
    #"*.avi")))
    file_path= filedialog.askopenfilename(title = "Select A File")
