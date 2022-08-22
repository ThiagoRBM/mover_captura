#!/usr/bin/env python3
import os
import time
import shutil

import settings


def mover(initial, final):
    name = f"captura_{settings.DATA.strftime('%Y_%m_%d_%H%M%S')}"
    extension = ".png"
    newname = final + "/" + name 
    n=0

    while True:
        n=n+1
        if n%500000==0:
            print("ouvindo")
        newfiles = os.listdir(initial)
        for file in newfiles:
            if extension in file:
                source = initial+"/"+file
                fileData= os.path.getctime(source)
                #print(fileData)
                if fileData >= settings.TIMESTAMP:
                    target = final
                    while os.path.exists(target):
                        target = f"{newname}_{n}_{extension}"
                    shutil.move(source, target)
                    print(f"arquivo {target} movido")
                time.sleep(1)
