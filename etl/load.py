# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 23:03:11 2025

@author: Elkin
"""
import pandas as pd

def save_data(data_frames, output_path):
    """Guarda los DataFrames limpios en un archivo Excel."""
    with pd.ExcelWriter(output_path) as writer:
        for sheet_name, df in data_frames.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
