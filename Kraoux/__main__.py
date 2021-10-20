###########
# MODULES #
###########

import os
import os.path
import subprocess
import urllib
from urllib import request
import time

###########################
# PATH AND URL DEFINITION #
###########################

PATH_DOWNLOAD = "C:\\temp"
os.makedirs(PATH_DOWNLOAD)

URL_DL_VSCODE = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"
# à ajouter : URL de DL pour NodeJS, JDK
# Prévoir liste contenant les 3 constantes, pour tout executer ?

#############
# FUNCTIONS #
#############

# Fonction pour télécharger la source depuis le site, vérifier si le téléchargement est fini puis executer la source (.exe) :
def download_and_execute(url):
    file_exist = False
    filename = request.urlopen(request.Request(url)).info().get_filename()
    urllib.request.urlretrieve(url, PATH_DOWNLOAD + "\\" + filename)
    time.sleep(3)
    while file_exist == False:
        if os.path.isfile(PATH_DOWNLOAD + "\\" + filename):
            os.startfile (PATH_DOWNLOAD + "\\" + filename)
            file_exist = True
            print ("File exist") # TEST TO BE REMOVED
        else:
            time.sleep(5)
            print ("File not exist") # TEST TO BE REMOVED

#############
# EXECUTION #
#############

download_and_execute(URL_DL_VSCODE)
