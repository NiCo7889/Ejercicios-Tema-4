"""
El comandante de la estrella de la muerte el gran Moff Tarkin debe administrar las asignaciones de vehículos y Stromtroopers a las distintas misiones que parten desde la 
estrella de la muerte, para facilitar esta tarea nos encomienda desarrollar las funciones necesarias para gestionar esto mediante prioridades de la siguiente manera:
- de cada misión se conoce su tipo (exploración, contención o ataque), planeta destino y general que la solicitó;
- si la misión fue pedida por Palpatine o Darth Vader su prioridad será baja;
- si la misión es de prioridad alta los recursos se asignarán manualmente independientemente de su tipo;
- si la misión es de baja prioridad se asignarán los recursos de la siguiente manera dependiendo de su tipo:
   * exploración: 15 Scout Troopers y 2 speeder bike, 
   * contención: 30 Stormtroopers y tres vehículos aleatorios (AT-AT, AT-RT, AT-TE, AT-DP, AT-ST) pueden ser repetidos,
   * ataque: 50 Stormtroopers y siete vehículos aleatorios (a los anteriores se le suman AT-M6, AT-MP, AT-DT),
- realizar la atención de todas las misiones y mostrar los recursos asignados a cada una, permitiendo agregar nuevos pedidos de misiones durante la atención;
- indicar la cantidad total de recursos asignados a las misiones.
"""

import random

class Mision:
    def __init__(self, tipo, destino, general):
        self.tipo = tipo
        self.destino = destino
        self.general = general
        self.alta_prioridad = general in ['Palpatine', 'Darth Vader']
        self.recursos = {'Stormtroopers': 0, 'Scout Troopers': 0, 'vehiculos': []}

    def asignar_recursos(self):
        if not self.alta_prioridad:
            vehiculos = ['AT-AT', 'AT-RT', 'AT-TE', 'AT-DP', 'AT-ST', 'AT-M6', 'AT-MP', 'AT-DT']
            if self.tipo == 'exploracion':
                self.recursos['Scout Troopers'] = 15
                self.recursos['vehiculos'] = ['speeder bike'] * 2
            elif self.tipo == 'contencion':
                self.recursos['Stormtroopers'] = 30
                self.recursos['vehiculos'] = random.choices(vehiculos[:5], k=3)
            elif self.tipo == 'ataque':
                self.recursos['Stormtroopers'] = 50
                self.recursos['vehiculos'] = random.choices(vehiculos, k=7)

class AdministradorMisiones:
    def __init__(self):
        self.misiones = []
        self.recursos_totales = {'Stormtroopers': 0, 'Scout Troopers': 0, 'vehiculos': 0}

    def agregar_mision(self, tipo, destino, general):
        mision = Mision(tipo, destino, general)
        mision.asignar_recursos()
        self.misiones.append(mision)
        self.actualizar_recursos(mision.recursos)

    def actualizar_recursos(self, recursos):
        for key in recursos:
            if key in ['Stormtroopers', 'Scout Troopers']:
                self.recursos_totales[key] += recursos[key]
            else:
                self.recursos_totales['vehiculos'] += len(recursos[key])

    def mostrar_recursos(self):
        for i, mision in enumerate(self.misiones):
            print(f'Misión {i + 1}: {mision.tipo} en {mision.destino} solicitada por {mision.general}')
            print('Recursos asignados:', mision.recursos)
            print()
        print('Recursos totales asignados:', self.recursos_totales)


administrador = AdministradorMisiones()

administrador.agregar_mision('exploracion', 'Tatooine', 'General Hux')
administrador.agregar_mision('contencion', 'Endor', 'Darth Vader')
administrador.agregar_mision('ataque', 'Hoth', 'Palpatine')

administrador.mostrar_recursos()
