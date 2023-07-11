import os
import shutil

fromDir = 'C:/Users/W10/Downloads/'
toDir = 'E:/Documentos/Arquivos_Documentos/'

fileList = os.listdir(fromDir)

for i in fileList:
    name,extension = os.path.splitext(i)
    
    if extension in ['.pdf']:
        path1 = fromDir + i
        path2 = toDir + 'Downloads'
        path3 = toDir + 'Downloads/' + i

        if os.path.exists(path2):
            print('movendo o arquivo ',i)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print('criando pasta Downloads ...')
            print('movendo o arquivo ',i)
            shutil.move(path1, path3)