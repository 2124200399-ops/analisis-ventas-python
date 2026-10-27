# 📊 Análisis Exploratorio de Datos de Ventas con Python & Pandas

Módulo de análisis de datos comerciales diseñado para la ingesta, limpieza, procesamiento y cálculo de estadísticas descriptivas a partir de registros transaccionales de ventas en formato Excel (.xlsx).

## 🚀 Tecnologías

- **Python 3.10+**
- **Pandas** (Estructuras de datos DataFrame y análisis estadístico)
- **OpenPyXL** (Procesamiento de hojas de cálculo de Excel)

## 📌 Funcionalidades Principales

- **Exploración de Estructura de Datos:** Inspección de dimensiones (shape), tipos de datos (info()) y primeros registros (head()).
- **Resumen Estadístico y Financiero:**
  - Conteo total de transacciones registradas.
  - Suma acumulada de precios unitarios.
  - Cálculo de precio unitario promedio (mean()), máximo (max()) y mínimo (min()).
  - Métricas de dispersión y distribución de datos mediante describe().

## ⚙️ Instalación y Ejecución

1. **Clonar repositorio:**
   `ash
   git clone https://github.com/2124200399-ops/analisis-ventas-python.git
   cd analisis-ventas-python
   `

2. **Crear y activar entorno virtual:**
   `ash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate
   `

3. **Instalar dependencias:**
   `ash
   pip install -r requirements.txt
   `

4. **Ejecutar el script de análisis:**
   `ash
   python app.py
   `

---
Proyecto desarrollado para el procesamiento y analítica descriptiva de datos de ventas.