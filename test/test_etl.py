# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 15:23:09 2025

@author: Elkin
"""

import pandas as pd
import pytest

from etl.extract import extract_data
from etl.transform import clean_numeric_column, clean_datetime_column, replace_null_with_nan, strip_whitespace
from etl.load import save_data

@pytest.fixture
def sample_data():
    data = {
        "id": ["1", "2", "NULL", "4"],
        "price": ["100", "200.5", "300,7", "invalid"],
        "date": ["2024-01-01 10:30:00", "NULL", "2023-12-31 23:59:59", "invalid"],
        "name": ["  Film A ", "Film B  ", "  NULL", "Film D"]
    }
    return pd.DataFrame(data)

def test_replace_null_with_nan(sample_data):
    df = replace_null_with_nan(sample_data)
    assert df.isna().sum().sum() > 0  # Debe haber valores NaN

def test_clean_numeric_column(sample_data):
    df = clean_numeric_column(sample_data)
    assert pd.api.types.is_numeric_dtype(df["price"])  # Debe ser numérico

def test_clean_datetime_column(sample_data):
    df = clean_datetime_column(sample_data)
    assert pd.api.types.is_datetime64_any_dtype(df["date"])  # Debe ser tipo fecha

def test_strip_whitespace(sample_data):
    df = strip_whitespace(sample_data)
    assert df["name"].str.startswith(" ").sum() == 0  # No debe haber espacios al inicio
