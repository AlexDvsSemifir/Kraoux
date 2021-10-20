###########
# MODULES #
###########

import os
import os.path
import subprocess
#from typing import ForwardRef
import urllib
from urllib import request
#from urllib.parse import urlparse
import time
import shutil

###########################
# PATH AND URL DEFINITION #
###########################

DESTINATION_DOWNLOAD = "C:\\temp"
os.makedirs(DESTINATION_DOWNLOAD)

URL_DL_VSCODE = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"
URL_DL_NODEJS = "https://nodejs.org/dist/v14.18.1/node-v14.18.1-x64.msi"
URL_DL_JDK = "https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe"

URL_LIST = [URL_DL_VSCODE, URL_DL_NODEJS, URL_DL_JDK]


#############
# FUNCTIONS #
#############

# Fonction pour télécharger la source depuis le site, vérifier si le téléchargement est fini puis executer la source (.exe) :
def download_and_execute(url):
    file_exist = False
    filename = request.urlopen(request.Request(url)).info().get_filename()
    if bool(filename) == 0:
        filename = os.path.basename(url)
    urllib.request.urlretrieve(url, DESTINATION_DOWNLOAD + "\\" + filename)
    time.sleep(3)
    while file_exist == False:
        if os.path.isfile(DESTINATION_DOWNLOAD + "\\" + filename):
            if ".msi" in filename:
                print("installation de " + filename + " en cours. Merci de patienter ...")
                subprocess.call('msiexec /i ' + DESTINATION_DOWNLOAD + "\\" + filename)
            else:
                print("Installation de " + filename + " en cours. Merci de patienter")
                subprocess.call(['runas', '/user:Administrateur', DESTINATION_DOWNLOAD + "\\" + filename])
            file_exist = True
        else:
            print ("Waiting for" + filename + "to download...")
            time.sleep(5)

#############
# EXECUTION #
#############

# i = 0
# while i < len(URL_LIST):
#     download_and_execute(URL_LIST[i])
#     i = i + 1
download_and_execute(URL_DL_JDK) # TEST TO BE REMOVED

shutil.rmtree(DESTINATION_DOWNLOAD)
