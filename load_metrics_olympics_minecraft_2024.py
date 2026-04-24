# ruff: noqa: E501, T201
import os

from google.cloud import bigquery

os.environ['GCP_PROJECT'] = 'anahi-staging'
GCP_PROJECT = os.getenv("GCP_PROJECT")
BQ_METRICS_DEFINITION_TABLE = f"{GCP_PROJECT}.metrics.metrics_definition"

bq_client = bigquery.Client(project=GCP_PROJECT)

METRICS_DEFINITION_DICT = {
    "comunication": {
        "metric_id": "comunication",
        "description": "Evalúa la claridad y precisión en la explicación del trabajo realizado basado en la novela. Considera la organización de la información presentada en el vídeo., score from 1 to 10",
        "modality": "video",
        "kind": "numeric",
        "requires_explanation": True,
        "implementation": "model",
        "args": """
            ========================
            Metric Name: comunication
            Description: Evalúa la claridad y precisión en la explicación del trabajo realizado basado en la novela. Considera la organización de la información presentada en el vídeo., score from 1 to 10
            Metric Type: numeric, score from 1 to 10 based on the table below. An explanation is required for the score decision. The explanation will be text and will be included in the output as a separate field as it shows the Output sample below.
            Score Table:
                |  Puntaje  | Comunicación |
                |-----------|--------------|
                |  **9-10** | Explica el trabajo realizado para resolver los desafíos de manera clara y fluida, usando términos precisos y mostrando un excelente dominio del tema. Incluye ejemplos visuales y verbales bien organizados y fáciles de seguir. |
                | **6-7-8** | Explica el trabajo realizado para resolver los desafíos de manera clara y utiliza la mayoría de los términos apropiados. El vídeo es fácil de seguir, aunque con algunos momentos de confusión. |
                | **3-4-5** | Se explica el trabajo realizado de manera comprensible, pero aparecen términos inexactos o desorganizados en ocasiones. El vídeo es difícil de seguir en algunas partes. |
                |  **1-2**  | Explicación poco clara y desorganizada. Usa términos incorrectos o no pertinentes y el vídeo es difícil de seguir. |
            Output Sample:
                '"comunication": 6,'
                '"comunication_explanation": "La explicación es comprensible y presenta algunas ideas organizadas, utilizando términos adecuados para el nivel esperado. Sin embargo, se observan repeticiones, omisiones relevantes o fragmentos poco claros que dificultan seguir el desarrollo completo del trabajo. Estas limitaciones justifican una puntuación en el nivel más bajo dentro del rango logrado.",'
        """,
    },
    "project_quality": {
        "metric_id": "project_quality",
        "description": "Evalúa la solución considerando los aspectos visuales, técnicos y de investigación que se aprecian al observar el vídeo., score from 1 to 10",
        "modality": "video",
        "kind": "numeric",
        "requires_explanation": True,
        "implementation": "model",
        "args": """
            ========================
            Metric Name: project_quality
            Description: Evalúa la solución considerando los aspectos visuales, técnicos y de investigación que se aprecian al observar el vídeo., score from 1 to 10
            Metric Type: numeric, score from 1 to 10 based on the table below. An explanation is required for the score decision. The explanation will be text and will be included in the output as a separate field as it shows the Output sample below.
            Score Table:
                |  Puntaje  | Nivel de la solución |
                |-----------|--------------|
                |  **9-10** | Excelente trabajo en lo que refiere a construcciones, ambientación y uso de la herramienta para modelar lo solicitado. |
                | **6-7-8** | El nivel de detalle es óptimo. Existen diferentes elementos de comunicación dentro del mundo que denota investigación y anclaje en la novela. |
                | **3-4-5** | Aparecen detalles en los interiores de las construcciones, personajes, y un contexto que revela algo de investigación. |
                |  **1-2**  | Las construcciones son muy básicas y carecen de nivel de detalle. |
            Output Sample:
                '"project_quality": 6,'
                '"project_quality_explanation": "El video muestra una solución que cumple con los aspectos básicos del desafío. Las construcciones principales están presentes y muestran cierto nivel de detalle, pero se observan limitaciones en la ambientación, el uso técnico de la herramienta o la incorporación de elementos que evidencien investigación contextual. La representación es adecuada, aunque no suficientemente desarrollada como para justificar una puntuación más alta dentro del rango logrado",'
        """,
    },
    "participation_colaboration": {
        "metric_id": "participation_colaboration",
        "description": "Expresión de entusiasmo como seña de identidad, más allá de los elementos físicos que posean. ¿Tiene logo y nombre del equipo? ¿Cómo se construyó esa identidad, en que se basaron? Apreciando las habilidades y contribuciones de todos los miembros de forma equilibrada, score from 1 to 10",
        "modality": "video",
        "kind": "numeric",
        "requires_explanation": True,
        "implementation": "model",
        "args": """
            ========================
            Metric Name: participation_colaboration
            Description: Expresión de entusiasmo como seña de identidad, más allá de los elementos físicos que posean. ¿Tiene logo y nombre del equipo? ¿Cómo se construyó esa identidad, en que se basaron? Apreciando las habilidades y contribuciones de todos los miembros de forma equilibrada, score from 1 to 10
            Metric Type: numeric, score from 1 to 10 based on the table below. An explanation is required for the score decision. The explanation will be text and will be included in the output as a separate field as it shows the Output sample below.
            Score Table:
                |  Puntaje  | Participación y Colaboración |
                |-----------|------------------------------|
                |  **9-10** | Demuestran alto entusiasmo con sólidas señas de identidad de equipo (nombre, logo, justificación de su identidad de equipo, presentación conjunta, etc.). Participación plenamente organizada, con tareas distribuidas de manera equilibrada entre todos los integrantes. Se valoran y articulan las habilidades individuales en función del objetivo común. |
                | **6-7-8** | Demuestran entusiasmo con claras señas de identidad. Participación organizada y tareas distribuidas entre la mayoría de los participantes del equipo. |
                | **3-4-5** | Demuestran entusiasmo con mínimas señas de identidad. Participación desorganizada o tareas distribuidas de forma desigual. |
                |  **1-2**  | Mínimo entusiasmo con escasas señas de identidad de equipo. No se detecta distribución y valorización de las tareas. Se visualiza la tarea de una sola persona del equipo. |
            Output Sample:
                '"participation_colaboration": 6,'
                '"participation_colaboration_explanation": "Se observa una participación organizada con entusiasmo generalizado. La mayoría de los integrantes intervienen en algún momento, aunque no todos tienen un rol claramente definido. Se menciona el nombre del equipo y se muestra un logo, pero no se identifican otros elementos narrativos que fortalezcan su identidad. La distribución de tareas es funcional pero no completamente equilibrada, lo que justifica una puntuación en el límite inferior del rango logrado",'
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
    result = "Rows inserted successfully."
else:
    result = "Rows insertion failed or returned unexpected result."
