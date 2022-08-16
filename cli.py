#!/usr/bin/env python3
import sys

import core

arguments= sys.argv[1:]

arg_dic= {}
for arg in arguments:
    key, value= arg.split("=")
    arg_dic[key]=value

if "initial" not in arg_dic.keys():
    print(f"Adicionar caminho do diretório a ser observado usando a palavra 'initial'")
    print(f"Palavras utilizadas: {arg_dic.keys()}")
    sys.exit(1)

if "final" not in arg_dic.keys():
    print(f"Adicionar caminho do diretório de final dos arquivos usando a palavra 'final'")
    print(f"Palavras utilizadas: {arg_dic.keys()}")
    sys.exit(2)

def moverCaptura(initial=arg_dic["initial"], final=arg_dic["final"]):
    """ Funcao que observa um diretório e move arquivos que tenham sido criados o início
    da sua execução para outro diretótio.

    initial: diretório a ser observado
    final: diretório para onde os arquivos serão movidos
    """
    core.mover(arg_dic["initial"],arg_dic["final"])