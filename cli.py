#!/usr/bin/env python3
import sys
import os

import core

arguments= sys.argv[1:]

arg_dic= {"initial": None,
            "final": None}
for arg in arguments:

    key, value= arg.split("=")
    arg_dic[key]=value

if arg_dic["initial"] == None:
    print(f"Adicionar caminho do diretório a ser observado usando 'initial='")
    print(f"Palavras utilizadas: {arg_dic.keys()}")
    sys.exit(1)

if arg_dic["final"] == None:
    arg_dic["final"]= os.path.abspath(os.curdir)
    print(f"Arquivos serão movidos para a pasta atual {arg_dic['final']}")
    #sys.exit(2)

def moverCaptura(initial=arg_dic["initial"], final=arg_dic["final"]):
    """ Funcao que observa um diretório e move arquivos que tenham sido criados após o início
    da sua execução para outro diretótio.

    initial: diretório a ser observado
    final: diretório para onde os arquivos serão movidos.
    """
    core.mover(arg_dic["initial"],arg_dic["final"])
