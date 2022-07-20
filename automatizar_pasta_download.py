import os
import shutil
import re

def fix_dir_expression(path):
    path = re.sub(r'[/|\\]{2,}|[\\]','/',path)
    return path

def listar():
    path = input('coloca a localizacao da pasta: ')
    path = fix_dir_expression(os.path.dirname(path))
    dir_path = os.listdir(path)

    for file in dir_path:
        path_complete = f'{path}/{file}'
        name, extension = os.path.splitext(file)
        extension = extension.replace('.', '').upper()

        if os.path.isdir(path_complete):
            continue
        
        if(os.path.exists(f'{path}/{extension}')):
            shutil.move(path_complete, f'{path}/{extension}/{file}')
        else:
            os.mkdir(f'{path}/{extension}')
            shutil.move(path_complete, f'{path}/{extension}/{file}')
        print('feito')

if __name__ == '__main__':
    listar()