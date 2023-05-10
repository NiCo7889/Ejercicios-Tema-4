"""
Se requiere implementar una red de ferrocarriles compuesta de estaciones de trenes y cambios de agujas (o desvíos). Contemplar las siguientes consideraciones:
- cada vértice del grafo no dirigido tendrá un tipo (estación o desvió) y su nombre, en el caso de los desvíos el nombre es un número, estos estarán numerados de manera consecutiva;
- cada desvío puede tener múltiples puntos de entrada y salida;
- se deben cargar seis estaciones de trenes y doce cambios de agujas;
- cada cambio de aguja debe tener al menos cuatro salida o vértices adyacentes;
- y cada estación como máximo dos salidas o llegadas y no puede haber dos estaciones co- nectadas directamente;
- encontrar el camino más corto desde:
    * la estación King's Cross hasta la estación Waterloo,
    * la estación Victoria Train Station hasta la estación Liverpool Street Station,
    * la estación St. Pancras hasta la estación King's Cross;
"""


import heapq
from typing import List, Tuple, Union


class Nodo:
    def __init__(self, nombre: str, tipo: str):
        self.nombre = nombre
        self.tipo = tipo
        self.vecinos = []

    def agregar_vecino(self, vecino: Tuple['Nodo', int]):
        self.vecinos.append(vecino)

class Estacion(Nodo):
    def __init__(self, nombre: str):
        super().__init__(nombre, 'estacion')

class Desvio(Nodo):
    def __init__(self, nombre: int):
        super().__init__(nombre, 'desvio')

class Grafo:
    def __init__(self, estaciones: List[Estacion], desvios: List[Desvio]):
        self.estaciones = estaciones
        self.desvios = desvios
        self.nodos = estaciones + desvios

    def conectar_nodos(self, nodo1: Nodo, nodo2: Nodo, distancia: int):
        nodo1.agregar_vecino((nodo2, distancia))
        nodo2.agregar_vecino((nodo1, distancia))

class CaminoMasCorto:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo

    def encontrar_camino(self, inicio: Union[Estacion, Desvio], fin: Union[Estacion, Desvio]) -> Tuple[List[Nodo], int]:
        visitados = set()
        distancias = {nodo: float('inf') for nodo in self.grafo.nodos}
        distancias[inicio] = 0

        cola_prioridad = [(0, inicio)]

        while cola_prioridad:
            dist_actual, nodo_actual = heapq.heappop(cola_prioridad)

            if nodo_actual not in visitados:
                visitados.add(nodo_actual)

                if nodo_actual == fin:
                    break

                for vecino, distancia in nodo_actual.vecinos:
                    nueva_distancia = dist_actual + distancia

                    if nueva_distancia < distancias[vecino]:
                        distancias[vecino] = nueva_distancia
                        heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        return distancias[fin]

# Crear estaciones y desvíos
estaciones = [Estacion("King's Cross"), Estacion('Waterloo'), Estacion('Victoria Train Station'), Estacion('Liverpool Street Station'), Estacion('St. Pancras'), Estacion('Paddington')]
desvios = [Desvio(i) for i in range(1, 13)]

# Conectar estaciones y desvíos según las restricciones
grafo = Grafo(estaciones, desvios)

grafo.conectar_nodos(estaciones[0], desvios[0], 7)
grafo.conectar_nodos(estaciones[0], desvios[1], 6)
grafo.conectar_nodos(estaciones[1], desvios[2], 8)
grafo.conectar_nodos(estaciones[1], desvios[3], 9)
grafo.conectar_nodos(estaciones[2], desvios[4], 4)
grafo.conectar_nodos(estaciones[2], desvios[5], 3)
grafo.conectar_nodos(estaciones[3], desvios[6], 5)
grafo.conectar_nodos(estaciones[3], desvios[7], 10)
grafo.conectar_nodos(estaciones[4], desvios[8], 2)
grafo.conectar_nodos(estaciones[4], desvios[9], 11)
grafo.conectar_nodos(estaciones[5], desvios[10], 12)
grafo.conectar_nodos(estaciones[5], desvios[11], 14)

for i in range(len(desvios) - 1):
    grafo.conectar_nodos(desvios[i], desvios[i + 1], 15)

# Encontrar caminos más cortos
camino_corto = CaminoMasCorto(grafo)

distancia1 = camino_corto.encontrar_camino(estaciones[0], estaciones[1])
distancia2 = camino_corto.encontrar_camino(estaciones[2], estaciones[3])
distancia3 = camino_corto.encontrar_camino(estaciones[4], estaciones[0])

print("Distancia desde King's Cross hasta Waterloo:", distancia1)
print("Distancia desde Victoria Train Station hasta Liverpool Street Station:", distancia2)
print("Distancia desde St. Pancras hasta King's Cross:", distancia3)
