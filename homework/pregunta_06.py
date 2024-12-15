"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_06():
    datos = pd.read_csv("files/input/tbl1.tsv", sep = '\t')
    unicas = sorted(datos["c4"].unique())
    return [x.upper() for x in unicas]       
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.tsv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
