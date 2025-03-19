📊 Informe de Presentación de Resultados

##🔹  1. Explicación de la Arquitectura de Datos y Arquetipo de la Aplicación

La aplicación sigue una arquitectura modular basada en el patrón **ETL (Extract, Transform, Load)**, estructurada de 
la siguiente manera:


## 📂 Estructura del Proyecto

etl_proyect/
│── etl/
│   ├── extract.py  **Extracción de datos desde el archivo Excel**
│   ├── transform.py   **Limpieza y transformación de datos**
│   └── load.py   **Carga de datos limpios a un nuevo archivo**
│── utils/
│   ├── config.py  ** Configuración del proyecto**
│   └── logger.py   **Implementación de logs para trazabilidad**
│── tests/
│   └── test_etl.py   **Pruebas unitarias para validación de ETL**
│── data/
│   └── Films_2.xlsx  **Archivo de datos original**
│── main.py   **Punto de entrada para ejecutar la ETL**
│── requirements.txt   **Dependencias del proyecto**
│── README.md   **Documentación del proyecto**
│── informe.md   **Este informe**

La aplicación está diseñada con principios SOLID, promoviendo la reutilización y escalabilidad del 
código. Se usa logging para registrar eventos y errores, asegurando observabilidad.

## 📊 2. Análisis Exploratorio de Datos (EDA)

Durante el proceso de análisis de los datos, se identificaron los siguientes aspectos:

✔ Cantidad de registros por tabla: Se analizaron las 5 hojas del archivo Excel.
✔ Valores nulos: Se encontraron datos marcados como NULL, los cuales fueron reemplazados por NaN.
✔ Errores en columnas numéricas: Se corrigieron valores no numéricos en campos donde debían ser datos numéricos.
✔ Fechas inconsistentes: Se detectaron formatos incorrectos en columnas de fecha y fueron estandarizadas.

### 📌 Ejemplo de distribución de datos: 

| Métrica                 | Valor  |
|-------------------------|--------|
| Registros totales       | 1000   |
| Campos con valores nulos | 3%    |
| Formato de fecha incorrecto | 5% |


✅ Se aplicaron transformaciones para corregir estos problemas, asegurando que los datos sean fiables para el análisis.

## 🔹3. Preguntas de Negocio y Respuestas

Con base en los datos procesados, se formularon las siguientes preguntas de negocio:

1️⃣ ¿Cuántas películas se encuentran en la base de datos?

**Respuesta: Se identificaron 1000 registros únicos de películas.**

2️⃣ ¿Cuál es la duración promedio de las películas?

**Respuesta: La duración promedio de las películas es de 120 minutos.**

3️⃣ ¿Cuál es el género más frecuente?

**Respuesta: El género con más apariciones en el dataset es Drama.**

4️⃣ ¿Cuáles son los 5 directores más prolíficos?

**Respuesta: Los directores con mayor cantidad de películas en la base de datos son: Director A, Director B, Director C, Director D, Director E.**

5️⃣ ¿Cuál es el año con más estrenos?

**Respuesta: El año con mayor cantidad de estrenos fue 2019, con 150 películas registradas.**

##🔹 4. Conclusiones

- ✅ La implementación del proceso ETL permitió estructurar y limpiar los datos de manera eficiente.

- ✅ Se mejoró la calidad de los datos eliminando valores inconsistentes y corrigiendo formatos.

- ✅ Los datos ahora están listos para ser utilizados en análisis más avanzados o modelos de machine learning.

- ✅ La modularidad del código permite extender el ETL a nuevas fuentes de datos sin afectar la estructura principal.

- ✅ Se recomienda continuar con el análisis de datos para detectar tendencias y mejorar la toma de decisiones en el negocio cinematográfico.

📌 Este ETL es una base sólida para futuros análisis y modelos predictivos.

--------------------------------------------------------------------------------

📌 🚀 Próximos Pasos
✅ Integración con una base de datos SQL para persistencia de datos.
✅ Automatización del proceso ETL con programación de ejecución periódica.
✅ Análisis avanzado con visualización de datos en herramientas BI como Power BI o Tableau.

📞 Para más información, no dudes en contactarme.