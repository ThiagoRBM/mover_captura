#!/usr/bin/env python3
import os
import time
import shutil

import settings


def mover(initial, final):
    name = f"captura_{settings.DATA.strftime('%Y_%m_%d_%H%M%S')}"
    extension = ".png"
    newname = final+"/" + name 

    while True:
        print("ouvindo")
        newfiles = os.listdir(initial)
        for file in newfiles:
            source = initial+"/"+file
            fileData= os.path.getctime(source)
            #print(fileData)
            if fileData >= settings.TIMESTAMP:
                n = 1
                target = newname
                while os.path.exists(target):
                    n = n+1 
                    target = f"{newname}_{n}_{extension}"
                shutil.move(source, target)
                print(f"arquivo {target} movido")
            time.sleep(1)

#     print(settings.DATA.strftime('%Y_%m_%d'))
#     print(initial)
#     print(final)
#     print("AAAAAA")