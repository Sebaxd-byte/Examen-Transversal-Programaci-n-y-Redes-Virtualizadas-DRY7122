
"""
Asignatura: Programación y Redes Virtualizadas (DRY7122)
Script: integrantes.py
Objetivo: Imprimir en pantalla la lista de integrantes del grupo de examen.
Integrantes: Sebastián Arcos y Jorge Manzo
"""

def desplegar_equipo():
    integrantes = [
        "Sebastián Arcos",
        "Jorge Manzo"
    ]

    print("\n" + "="*45)
    print("      INTEGRANTES DEL EQUIPO DE EXAMEN")
    print("="*45)

    for numero, nombre in enumerate(integrantes, start=1):
        print(f" {numero}. {nombre}")
    print("="*45 + "\n")

if __name__ == "__main__":
    desplegar_equipo()

