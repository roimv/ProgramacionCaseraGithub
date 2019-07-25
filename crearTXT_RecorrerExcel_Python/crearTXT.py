import os
from os import walk
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
# Se parte de un archivo Excel que tiene diferentes registros(=elementos) que queremos copiar y crear un archivo de texto con el nombre de ese elemento y su código consecutivo
titulo = 'tituloExcel'
directorio = 'C:\prueba'
carpeta = os.path.join(directorio, titulo)
xlsOld = os.path.join(carpeta, titulo) + ".xls"
xls = pd.ExcelFile(xlsOld)
df = pd.read_excel(xls, sheet_name='nombreHoja')
dcPDI = pd.read_excel(xls, sheet_name= titulo)


for i in df.index:
    desc = df['descripcionQueTengaElElemento'][i]
    # Se crea el archivo y se coloca el código que deseamos (Ej: "Ejemplo01_Desc.txt")
    file = open("C:\CarpetaCrearTXT\ejemplo" + str(i) + "_" + str(desc) + ".txt", "w")

# Ahora hay que añadir un "0" (Cero) a los primeros 9 documentos de texto y borrar un "0" (Cero) a partir del número 100 antes de abrir el siguiente script ("introPDI")