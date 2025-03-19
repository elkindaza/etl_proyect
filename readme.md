


# Proyecto ETL 

Este proyecto implementa una **ETL (Extract, Transform, Load)** en Python para procesar datos de películas desde
un archivo Excel (`Films_2 .xlsx`). Se eliminan inconsistencias, se transforman formatos incorrectos
y se exporta un archivo limpio (`Films_cleaned.xlsx`).

##  Requisitos  
- **Python 3.8+**  
- **Librerías:** Pandas, Pytest, OpenPyXL  

## Estructura del Proyecto  

etl_proyect/ 

    ── etl/  
        ── extract.py 
        ── transform.py
        ── load.py 
        
    ── utils/  
        ── config.py  
        ── logger.py 
        
    ── tests/  
        ── test_etl.py 
        
    ── data/ 
        ── Films_2.xlsx 
        
    ── main.py 
    ── requirements.txt 
    ── README.md 
    ── informe.md
    
##  Cómo Ejecutar la ETL  
1️. Instalar dependencias:  

    pip install -r requirements.txt
    
2. Ejecutar la ETL:

    python main.py

## 🧪 Cómo Ejecutar las Pruebas  
Para validar el correcto funcionamiento del ETL, ejecuta:  
``bash
pytest -v tests/test_etl.py

## Tecnologías Utilizadas  

- **Python** (Lenguaje de programación)  
- **Pandas** (Procesamiento de datos)  
- **Logging** (Para trazabilidad y monitoreo)  
- **Pytest** (Framework para pruebas unitarias)  

## Autor

Elkin Javier Daza Aullon
e.daza@udla.edu.co
3142300320