import os
from os import walk
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
# el nombre de la hoja del excel con los elementos debe llamarse igual que la carpeta que lo engloba para correr este script
titulo = 'tituloExcel'
directorio = 'C:\prueba'
carpeta = os.path.join(directorio, titulo)
xlsOld = os.path.join(carpeta, titulo) + ".xls"
xls = pd.ExcelFile(xlsOld)
df = pd.read_excel(xls, sheet_name='nombreHoja')
dcPDI = pd.read_excel(xls, sheet_name= titulo)

# Se corre un For para poder introducir dentro de los archivos creados anteriormente la información que deseamos, con especificaciones concretas

for dirName, subdirList, archivos in os.walk(carpeta):
    for nombre in archivos:
        ruta = os.path.join(carpeta, nombre)
        for i in dcPDI.index:
            pdi = dcPDI['descripcionQueTenga'][i]
            segundoElemento = dcPDI['segundoElementoEnExcel'][i]
            tercerElemento = dcPDI['tercerElementoEnExcel'][i]
            if nombre[-4:] == r".txt":
                documento = open(ruta, "a")
                if tercerElemento == nombre[:7]:
                    documento.write(str(pdi) + " " + "\t" + str(segundoElemento) + os.linesep)
                    documento.close()
                    i = i+1
                else:
                    i = i+1


