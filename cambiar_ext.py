'''
Author: David Luna
        PhD. Student at the University of Antioquia
        SISTEMIC
Description: Cambia la extensión de un archivo y agregar prefijos
version: 1.1
'''

import os
import argparse
from pathlib import Path
from tqdm import tqdm


argparser = argparse.ArgumentParser(description='Cambiar extension de archivos')
argparser.add_argument('-p', '--path',required=True, help='Ruta donde se encuentran los archivos')

args = argparser.parse_args()

files = list(Path(args.path).rglob('*.*'))

for file  in tqdm(files):
    sfile = str(file).split('/')
    pref = sfile[-2]
    filename = file.name
    ext = filename.split('.')[-1]

    os.rename(file, file.with_name(f'{pref}_{file.name}'))

    if ext != ext.lower():
        new_file = file.parent.joinpath(f'{pref}_{file.name}')
        os.rename(new_file, new_file.with_suffix(f'.{ext.lower()}'))




