import os
import shutil

from_dir = "C:/Users/PC PERFORMANCE/Downloads"
to_dir = "C:/Users/PC PERFORMANCE/Documents/byjus/Arquivos_Documentos"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
    nome,extensao=os.path.splitext(i)
    print(i)

    if (i=="torredepisa.jpg"):
        shutil.move(from_dir+"/"+i, to_dir+"/" +i)
    
    
