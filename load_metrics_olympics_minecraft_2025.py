# ruff: noqa: E501, T201
import os

from google.cloud import bigquery

os.environ['GCP_PROJECT'] = 'anahi-staging'
GCP_PROJECT = os.getenv("GCP_PROJECT")
BQ_METRICS_DEFINITION_TABLE = f"{GCP_PROJECT}.metrics.metrics_definition"

bq_client = bigquery.Client(project=GCP_PROJECT)

METRICS_DEFINITION_DICT = {
    "semaforo": {
        "metric_id": "semaforo",
        "description": "Clasifica a cada equipo en tres niveles (Inicial, Desarrollo, Logrado) a partir de la evidencia observable en el video.",
        "modality": "video",
        "kind": "categorical",
        "implementation": "model",
        "requires_explanation": True,
        "args": """
            ========================
            Metric Name: semaforo
            Description: Clasifica a cada equipo en tres niveles (Inicial, Desarrollo, Logrado) a partir de la evidencia observable en el video.
            Metric Type: categorical. Categories: Inicial, Desarrollo, Logrado. An explanation is required for the decision. The explanation will be text and will be included in the output as a separate field as it shows the Output sample below.
            Categories:
                - Inicial:
                    * Cumplimiento parcial o mínimo de la consigna. Explicación poco clara, desordenada o muy breve.
                    * Recreación/ambientación básica, poco coherente o escasamente evidenciada; o presentación de equipo superficial, sin identidad definida.
                    * Participación limitada o centrada en una sola persona, sin distribución visible de tareas.
                - Desarrollo:
                    * Cumple la consigna principal. Explicación mayormente clara, con pequeñas lagunas u organización irregular por momentos.
                    * Recreación/ambientación con buen nivel general pero con ausencias o inconsistencias puntuales; o identidad de equipo mencionada pero poco desarrollada.
                    * Participación mayoritaria; algunos integrantes con menor visibilidad o roles difusos.
                - Logrado:
                    * Explicación clara, ordenada y precisa del proyecto; se justifican decisiones y/o se mencionan fuentes o evidencias.
                    * Recreación/ambientación histórica coherente y detallada (p. ej., edificios/ubicaciones aproximadas, escenas, NPC/oficios/diálogos integrados), una identidad de equipo nítida y bien articulada.
                    * Participación visible y equilibrada de integrantes o roles claramente identificables.
            Output Sample:
                '"semaforo": "Desarrollo",'
                '"semaforo_explanation": "La explicación cubre los aspectos principales y se observa ambientación histórica con elementos reconocibles. Sin embargo, hay secciones desordenadas y la participación no es equilibrada. Por ello, corresponde 'En desarrollo'.",'

        """,
    },

    "great_work": {
        "metric_id": "great_work",
        "description": "Comentario breve y positivo para el equipo, destacando aspectos concretos del video.",
        "modality": "video",
        "kind": "text",
        "requires_explanation": False,
        "implementation": "model",
        "args": """
            ========================
            Metric Name: great_work
            Description: Genera un comentario breve dirigido al equipo, resaltando logros observables en el video. 
            Metric Type: text

            Reglas:
            - Obligatoria: el comentario no puede quedar vacío.
            - Tono: positivo, concreto y específico; evitar vaguedades (“muy bueno”) sin evidencia.
            - Extensión: 1–3 oraciones (≈ 20–50 palabras).
            - Contenido: mencionar 1–3 aspectos observables y positivos.
            - No debe comenzar con “Buen trabajo en” o “Gran trabajo en” (eso ya está preimpreso en la rúbrica).
            - No incluir sugerencias de mejora, evaluaciones numéricas ni comparaciones entre equipos.
            - Basarse únicamente en lo que se ve/escucha en el video.

            Aspectos posibles (ejemplos, solo si se observan):
            - Claridad y organización de la explicación; uso de términos adecuados; integración de ejemplos visuales/verbales.
            - Participación visible y equilibrada; identidad del equipo (nombre/logo/relato).
            - Recreación/ambientación histórica (edificios, ubicación aproximada, NPC/oficios/diálogos).
            - Recursos del video: narración/locución clara, subtítulos, edición que facilita seguir el relato.

            Output Sample:
                "great_work": "La claridad del relato y la integración de imágenes que muestran las construcciones de manera comprensible. También se aprecia la participación equilibrada de los integrantes con una identidad de equipo definida."
        """,
    },
    "think_about": {
        "metric_id": "think_about",
        "description": "Sugerencias de mejora para el equipo, indicando uno o más aspectos a considerar a partir del video.",
        "modality": "video",
        "kind": "text",
        "requires_explanation": False,
        "implementation": "model",
        "args": """
            ========================
            Metric Name: think_about
            Description: Genera un comentario breve dirigido al equipo con foco en sugerencias de mejora. 
            Metric Type: text

            Reglas:
            - Obligatoria: el comentario no puede quedar vacío.
            - Tono: constructivo, claro y específico; evitar frases vagas (“se puede mejorar en todo”).
            - Extensión: 1–3 oraciones (≈ 20–70 palabras).
            - Contenido: mencionar uno o varios aspectos concretos a mejorar, todos factibles de implementar.
            - No debe comenzar con “Piensen en” o “Think about” (eso ya estará en la rúbrica).
            - No incluir elogios aquí (van en `great_work`), ni evaluaciones numéricas.
            - Basarse únicamente en lo que se observa/escucha en el video.

            Aspectos posibles (ejemplos, solo si se detectan):
            - Claridad y organización del relato.
            - Participación más equilibrada de los integrantes (dar espacio visible a todos).
            - Inclusión de más elementos históricos relevantes (edificios, personajes, ambientación, diálogos).
            - Profundizar en la ambientación y los detalles del mundo construido (ej.: calles, oficios, escenas cotidianas).

            Output Sample:
                "think_about": "Ampliar la participación visible de todos los integrantes y añadir más detalles en la ambientación histórica."
        """,
    },


    "participacion_colaboracion_2025": {
        "metric_id": "participacion_colaboracion_2025",
        "description": "Expresión de entusiasmo como seña de identidad, más allá de los elementos físicos que posean. ¿Tiene logo y nombre del equipo? ¿Cómo se construyó esa identidad, en que se basaron? Apreciando las habilidades y contribuciones de todos los miembros de forma equilibrada, score from 1 to 10",
        "modality": "video",
        "kind": "numeric",
        "requires_explanation": True,
        "implementation": "model",
        "args": """
            ========================
            Metric Name: participacion_colaboracion_2025
            Description: Expresión de entusiasmo como seña de identidad, más allá de los elementos físicos que posean. ¿Tiene logo y nombre del equipo? ¿Cómo se construyó esa identidad, en que se basaron? Apreciando las habilidades y contribuciones de todos los miembros de forma equilibrada, score from 1 to 10
            Metric Type: numeric, score from 1 to 10 based on the table below. An explanation is required for the score decision. The explanation will be text and will be included in the output as a separate field as it shows the Output sample below.
            Score Table:
                |  Puntaje  | Participación y Colaboración |
                |-----------|------------------------------|
                |  **9-10** | Se evidencia una participación activa de todo el equipo, con aportes de cada uno de los integrantes. El equipo muestra gran entusiasmo, creatividad y una identidad clara. Explican cómo se organizaron, qué aprendieron y cómo enfrentaron el desafío. |
                | **6-7-8** | Demuestran entusiasmo con claras señas de identidad. Participación organizada y tareas distribuidas entre la mayoría de los participantes del equipo. |
                | **3-4-5** | Demuestran entusiasmo con mínimas señas de identidad. Participación desorganizada o tareas distribuidas de forma desigual. |
                |  **1-2**  | Mínimo entusiasmo con escasas señas de identidad de equipo. No se detecta distribución y valorización de las tareas. Se visualiza la tarea de una sola persona del equipo. |
            Output Sample:
                '"participacion_colaboracion_2025": 6,'
                '"participacion_colaboracion_2025_explanation": "Se observa una participación organizada con entusiasmo generalizado. La mayoría de los integrantes intervienen en algún momento, aunque no todos tienen un rol claramente definido. Se menciona el nombre del equipo y se muestra un logo, pero no se identifican otros elementos narrativos que fortalezcan su identidad. La distribución de tareas es funcional pero no completamente equilibrada, lo que justifica una puntuación en el límite inferior del rango logrado",'
        """,
    },
}

try:
    result = bq_client.insert_rows_json(
        table=BQ_METRICS_DEFINITION_TABLE,
        json_rows=[value for _, value in METRICS_DEFINITION_DICT.items()],
    )
except Exception as e:  # noqa: BLE001
    result = f"Error inserting rows: {e}"
if isinstance(result, list) and len(result) == 0:
    print("Rows inserted successfully.")
else:
    print("Rows insertion failed or returned unexpected result.")
    print(result)
