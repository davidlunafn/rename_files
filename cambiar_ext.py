'''
Author: David Luna
        PhD. Student at the University of Antioquia
        SISTEMIC
Description: Cambia la extensión de un archivo y agregar prefijos
version: 1.1
'''

import os
import time
from datetime import timedelta
import argparse
from pathlib import Path


argparser = argparse.ArgumentParser(description='Cambiar extension de archivos')
argparser.add_argument('-p', '--path',required=True, help='Ruta donde se encuentran los archivos')

args = argparser.parse_args()


formatos = ['wav', 'WAV']
Numero_grab = 0
print(f"Inventorying Files...")
start_time = time.time()
for (root, dirs, file) in os.walk(args.path):

    if len(dirs) == 0:
        files = list(Path(root).rglob('*.{}'.format(formatos[1])))

        #Cambiar extension    
        for x in files:
            os.rename(x, x.with_suffix(f'.{formatos[0]}'))
        
        files = list(Path(root).rglob('*.{}'.format(formatos[0])))

        #Agregar prefijo
        for x in files:
            os.rename(x, x.with_name(f'{os.path.basename(root)}_{x.name}'))
            Numero_grab = Numero_grab + 1

print(f"{Numero_grab} files found")
print('realizado')
print(f"Execution Time {str(timedelta(seconds=time.time() - start_time))}")
