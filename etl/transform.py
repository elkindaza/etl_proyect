# -*- coding: utf-8 -*-
import pandas as pd
import re


def clean_numeric_column(df):
   
    # Iterar sobre todas las columnas del DataFrame
    for col in df.columns:
        # Verificar si la columna debería ser numérica (contiene principalmente números)
        if pd.to_numeric(df[col], errors='coerce').notna().any():
            # Convertir a texto para limpiar
            df[col] = df[col].astype(str)

            # Reemplazar comas por puntos (para decimales)
            df[col] = df[col].str.replace(',', '.', regex=False)

            # Eliminar caracteres no numéricos (excepto el punto decimal)
            df[col] = df[col].apply(lambda x: re.sub(r'[^0-9.]', '', x))

            # Convertir a número (NaN si no es convertible)
            df[col] = pd.to_numeric(df[col], errors='coerce')
          
    return df


def clean_datetime_column(df):
    
    # Patrón para detectar fechas con horas (por ejemplo, "YYYY-MM-DD HH:MM:SS")
    date_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

    # Iterar sobre todas las columnas del DataFrame
    for col in df.columns:
        # Verificar si la columna contiene cadenas que coinciden con el patrón de fecha
        if df[col].astype(str).str.contains(date_pattern).any():
            # Reemplazar "null" con NaN
            df[col] = df[col].replace("NULL", pd.NA)

            # Convertir la columna a tipo datetime
            df[col] = pd.to_datetime(df[col], errors='coerce')
    return df

    

def replace_null_with_nan(df):
    
    # Reemplazar "NULL" con NaN en todas las columnas
    df = df.replace(r"^\s*NULL\s*$", pd.NA, regex=True)  # ✅ Maneja espacios y variaciones
    
    return df

def strip_whitespace(df):
    
    
    # Iterar sobre todas las columnas del DataFrame
    for col in df.columns:
        # Verificar si la columna es de tipo objeto (texto)
        if df[col].dtype == 'object':
            # Eliminar espacios en blanco al principio y al final
            df[col] = df[col].str.strip()
    return df
    