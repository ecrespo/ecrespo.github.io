#!/usr/bin/env python3

from typing import Literal, Dict


GENERO = Literal["hombre", "mujer", "no especificado"]


def crear_usuario(
    nombre: str,
    apellido: str,
    genero: GENERO,
) -> Dict[str, str]:
    return {
        "nombre": nombre,
        "apellido": apellido,
        "genero": genero
    }


crear_usuario("John", "Doe", "hombre")
crear_usuario("Jane", "Doe", "mujer")
crear_usuario("John", "Doe", "x")
