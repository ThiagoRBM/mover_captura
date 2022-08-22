#!/usr/bin/env python3
import os
import time
from datetime import date,datetime
import shutil

import settings


def mover(initial, final):
    #name = f"captura_{settings.DATA.strftime('%Y_%m_%d_%H%M%S')}"
    extension = ".png"
    #newname = final + "/" + name 
    n=0

    while True:
        newfiles = os.listdir(initial)
        for file in newfiles:
            if extension in file:
                source = initial+"/"+file
                fileData= os.path.getctime(source)
                #print(file, fileData)
                if fileData >= settings.TIMESTAMP:
                    n=n+1
                    newname= (f"captura_"
                            f"{datetime.fromtimestamp(fileData).strftime('%Y_%m_%d_%H%M%S')}")
                    print("novo",newname)
                    target = final
                    while os.path.exists(target):
                        target = f"{newname}_{n}_{extension}"
                    shutil.move(source, target)
                    print(f"arquivo {target} movido")
                print("ouvindo")
                time.sleep(5)
