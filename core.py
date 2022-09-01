#!/usr/bin/env python3
import os
import time
from datetime import date,datetime
import shutil

import settings


def mover(initial, final=None):
    extension = ".png"
    n=0
    while True:
        newfiles = os.listdir(initial.strip())
        for file in newfiles:
            if extension in file:
                source = initial+"/"+file
                fileData= os.path.getctime(source)
                #print(file, fileData)
                if fileData >= settings.TIMESTAMP:
                    n=n+1
                    newname= (f"captura_"
                            f"{datetime.fromtimestamp(fileData).strftime('%Y_%m_%d_%H%M%S')}")
                    #print("novo",newname)
                    target = final.strip()
                    while os.path.exists(target):
                        target = f"{newname}_{n}_{extension}"
                    shutil.move(source, target)
                    time.sleep(1)
                    print(f"arquivo {target} movido para {final}")
                if time.time() % 5 == 0:
                    print("ouvindo")
