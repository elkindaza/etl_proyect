# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 23:06:41 2025

@author: Elkin
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Ruta base del proyecto
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "../data"))  # Asegura la ruta absoluta
INPUT_FILE = os.path.join(DATA_DIR, "Films_2 .xlsx")  # ✅ Sin espacio extra en el nombre
OUTPUT_FILE = os.path.join(DATA_DIR, "Films_cleaned.xlsx")

# Configuración de logging
LOG_LEVEL = "INFO"


# Verificar si el archivo existe
if os.path.exists(INPUT_FILE):
    print("✅ El archivo existe.")
else:
    print("❌ ERROR: No se encuentra el archivo Films_2 .xlsx")
