from genericpath import exists
import string
import random
import datetime
import tempfile
import os
from pyautogui import screenshot 

def takeScreenshot():
    try:
        path_to_dir = tempfile.gettempdir() + "/screenshots"
        path_to_logfile = path_to_dir + "/screenshots.log"
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(10))

        myScreenshot = screenshot()
        myScreenshot.save(path_to_dir + "/" + name + '.png')
        if not exists(path_to_dir):
            os.mkdir(path_to_dir)
            
        # should be saved to temp dir
        with open(path_to_logfile, "a") as file:
            file.write(str(datetime.datetime.now()) + "\n")

    except Exception as e:
        pass

#takeScreenshot()
