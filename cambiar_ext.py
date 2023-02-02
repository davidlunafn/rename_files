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
argparser.add_argument('-d', '--delete_prefix',required=False, default=False, help='Borrar prefijo de los audios')

args = argparser.parse_args()

Numero_grab = 0
print(f"Inventorying Files...")
start_time = time.time()
for (root, dirs, file) in os.walk(args.path):
    if len(dirs) == 0:
        files = list(Path(root).rglob('*.*'))

        if args.delete_prefix == False:
            for x in files:
                filename = x.name
                ext = filename.split('.')[-1]
                new_name =  x.with_name(f'{os.path.basename(root)}_{x.name}').with_suffix(f'.{ext.lower()}')
                os.rename(x,new_name)
                Numero_grab = Numero_grab + 1
        else:
            for x in files:
                filename = x.name
                base_name = '_'.join(filename.split('_')[-2:])
                new_name = x.with_name(base_name)
                os.rename(x,new_name)
                Numero_grab = Numero_grab + 1

print(f"{Numero_grab} files found")
print('realizado')
print(f"Execution Time {str(timedelta(seconds=time.time() - start_time))}")
