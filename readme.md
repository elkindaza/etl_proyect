
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


##📚 Justificación del Diseño

La aplicación sigue una arquitectura modular basada en el patrón ETL (Extract, Transform, Load), lo que permite una separación clara de responsabilidades y facilita la escalabilidad del proyecto. Se han aplicado principios SOLID, garantizando un código limpio y reutilizable.

**Modularidad**: Separación clara de extracción, transformación y carga en archivos individuales.

**Observabilidad**: Implementación de logging para registrar eventos, facilitando la depuración y monitoreo.

**Configurabilidad**: Uso de config.py para manejar rutas y configuraciones de manera centralizada.


##🔬 Detalle de la Implementación

📂 Extracción (extract.py)

Carga los datos desde un archivo Excel (Films_2.xlsx) y los almacena en DataFrames de Pandas, permitiendo su manipulación posterior.

📂 Transformación (transform.py)

Realiza limpieza y transformación de datos, incluyendo:

Eliminación de valores nulos (NULL).

Corrección de valores numéricos mal formateados.

Estandarización de formatos de fecha.

📂 Carga (load.py)

Guarda los datos procesados en un nuevo archivo Excel (Films_cleaned.xlsx).

📂 Ejecución (main.py)

Controla el flujo del ETL, llamando a los módulos en orden y asegurando que los datos pasen por todas las etapas correctamente.

📂 Pruebas (test_etl.py)

Contiene pruebas unitarias con pytest para validar que las transformaciones de datos funcionan correctamente. 

## Autor

Elkin Javier Daza Aullon
e.daza@udla.edu.co
3142300320
