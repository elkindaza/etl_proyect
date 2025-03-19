# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 23:02:18 2025

@author: Elkin
"""

import pandas as pd

def extract_data(file_path):
    """Carga todas las hojas de un archivo Excel en un diccionario de DataFrames."""
    xls = pd.ExcelFile(file_path)
    data_frames = {sheet: pd.read_excel(xls, sheet_name=sheet) for sheet in xls.sheet_names}
    return data_frames
