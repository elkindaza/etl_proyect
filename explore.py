# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 22:42:33 2025

@author: Elkin
"""

import pandas as pd


# Ruta del archivo Excel
file_path = "Films_2 .xlsx"



# Cargar el archivo Excel
xls = pd.ExcelFile(file_path)

# Ver nombres de las pestañas
print("Pestañas disponibles:", xls.sheet_names)

# Cargar y visualizar la primera tabla
df = pd.read_excel(xls, sheet_name=xls.sheet_names[2])
print(df.head())  # Muestra las primeras 5 filas

# Cargar y visualizar la primera tabla
df = pd.read_excel(xls, sheet_name=xls.sheet_names[3])
print(df.head())  # Muestra las primeras 5 filas

# Cargar y visualizar la primera tabla
df = pd.read_excel(xls, sheet_name=xls.sheet_names[4])
print(df.head())  # Muestra las primeras 5 filas