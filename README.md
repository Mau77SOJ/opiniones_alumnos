# Informe técnico del análisis de corpus educativo
## Descripción general
Se realizó un análisis de un corpus textual compuesto por opiniones de estudiantes sobre el modelo de educación que sueñan para el año 2025 en Colombia. El objetivo fue procesar lingüísticamente el texto en español y visualizar los patrones más frecuentes mediante N-gramas.

## Herramientas y tecnologías utilizadas
- Lenguaje de programación: Python
- Librerías:
- spaCy: procesamiento de lenguaje natural (modelo es_core_news_sm)
- NLTK: gestión de stopwords en español
- Scikit-learn: vectorización del texto con CountVectorizer
- Matplotlib: visualización de resultados
- Pandas: manejo estructurado de frecuencias

## Flujo de trabajo del código
- Carga de corpus:
- Lectura del archivo CorpusEducacion.txt con texto libre de opiniones estudiantiles.
- Preprocesamiento textual:
- Tokenización: uso de spaCy para dividir el texto en unidades mínimas (tokens).
- Filtrado de stopwords y símbolos: eliminación de palabras vacías (con NLTK) y caracteres irrelevantes (definidos manualmente).
- Lematización: normalización de palabras a su raíz gramatical para evitar redundancia.
- Vectorización:
- Transformación del corpus en vectores utilizando CountVectorizer.
- Configuración del rango de N-gramas en bigramas y trigramas (2,3).
- Visualización:
- Generación de un gráfico de barras horizontales (barh) con los 10 N-gramas más frecuentes.

## Resultados
Se identificaron los siguientes patrones dominantes:
| N-Grama | Frecuencia estimada | 
| sueño educación | Alta | 
| educación calidad | Media-Alta | 
| educación inclusiva | Media | 
| institución educativa | Media | 
| educación 2025 | Media | 


## Estos resultados reflejan un enfoque aspiracional hacia:
- Calidad y equidad educativa
- Inclusión social en la formación
- Infraestructura institucional
- Futuro proyectado (año 2025)
- Rol protagónico de la educación como herramienta de transformación

## Evaluación del corpus
- El corpus revela una carga semántica alta en torno a valores como igualdad, participación, infraestructura, formación docente y reconocimiento cultural.
- La narrativa está marcada por el uso reiterado del verbo “soñar”, lo que define la tonalidad del texto como propositiva y emocionalmente comprometida.
- Las menciones a “Colombia”, “calidad”, “niños”, “paz”, “valores”, y “tecnología” aparecen como componentes transversales que conectan los distintos testimonios.
