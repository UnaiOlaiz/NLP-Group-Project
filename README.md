# NLP Group Project – CoranNLP

Un proyecto de **procesamiento del lenguaje natural (NLP)** aplicado al análisis del Corán en árabe e inglés. El objetivo es preparar, analizar y procesar los textos religiosos para desarrollar un sistema de **búsqueda semántica** avanzado.

---

## Tabla de Contenidos

- [Descripción](#descripción)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Recursos](#recursos)

---

## Descripción

CoranNLP es un proyecto que implementa técnicas de NLP para:

- Procesar y limpiar textos del Corán en árabe e inglés
- Realizar análisis lingüístico y estadístico de los textos sagrados
- Preparar el corpus para búsqueda semántica
- Aplicar herramientas especializadas de NLP para lengua árabe

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Anaconda** o **Miniconda**
- **Python 3.x** (la versión específica se define en `environment.yml`)
- **Git** (para clonar el repositorio)

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd CoranNLP
```

### 2. Crear el entorno conda

El entorno completo está definido en `env/environment.yml`:

```bash
conda env create -f env/environment.yml
```

### 3. Activar el entorno

```bash
conda activate coran_nlp
```

---

## Estructura del Proyecto

```
CoranNLP/
├── data/
│   ├── raw_data/          # Textos originales del Corán
│   └── cleaned_data/      # Textos procesados (generados)
├── src/
│   ├── prepare_data.py    # Script de limpieza y preparación
│   └── E1 - Análisis de los Datos.ipynb  # Notebook de análisis
│   └── CoranNLP.ipynb # Notebook embeddings
├── env/
│   └── environment.yml    # Definición del entorno conda
└── README.md
```

---

## Uso

### Paso 1: Preparación de los datos

Ejecuta el script de preparación para limpiar y procesar los textos:

```bash
python src/prepare_data.py
```

Este script generará los archivos procesados en el directorio `data/cleaned_data/`.

### Paso 2: Análisis de los datos

Abre y ejecuta el notebook de Jupyter para realizar el análisis:

```bash
jupyter notebook src/E1\ -\ Análisis\ de\ los\ Datos.ipynb
```

O si prefieres JupyterLab:

```bash
jupyter lab
```

### Funcionalidades principales

- **Limpieza de texto**: Normalización, eliminación de diacríticos, tokenización
- **Análisis estadístico**: Frecuencia de palabras, longitud de versículos, distribución léxica
- **Procesamiento bilingüe**: Manejo paralelo de textos en árabe e inglés
- **Preparación para embeddings**: Formato adecuado para modelos de búsqueda semántica

---

## Recursos

### Herramientas de NLP en Árabe

- [**CAMeL Tools Documentation**](https://camel-tools.readthedocs.io/) – Librería especializada para procesamiento del lenguaje natural en árabe

## Licencia

Este proyecto es de código abierto y está disponible para fines educativos y de investigación.

---

**Desarrollado con <3 para el análisis lingüístico del Corán y adoración del mismo**
