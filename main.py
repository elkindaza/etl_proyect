
from etl.extract import extract_data
from etl.transform import clean_numeric_column, clean_datetime_column, replace_null_with_nan, strip_whitespace
from etl.load import save_data
from utils.logger import logger
from utils.config import INPUT_FILE, OUTPUT_FILE  # Importamos las rutas desde config.py

logger.info("Iniciando proceso ETL...")

# Cargar los datos
data = extract_data(INPUT_FILE)

# Verificar que los datos se hayan cargado correctamente
if not data:
    logger.error(f"No se pudo cargar el archivo: {INPUT_FILE}")
    exit(1)

# Limpiar las columnas en cada hoja
cleaned_data = {}
for sheet, df in data.items():
    logger.info(f"Limpieza de la hoja: {sheet}")
    df = replace_null_with_nan(df)
    df = clean_numeric_column(df)
    df = clean_datetime_column(df)
    df = strip_whitespace(df)
    cleaned_data[sheet] = df

# Guardar los datos limpios
save_data(cleaned_data, OUTPUT_FILE)

logger.info(f"Proceso ETL finalizado con éxito. Archivo guardado en {OUTPUT_FILE}")


