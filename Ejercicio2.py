"""
El comandante de la estrella de la muerte el gran Moff Tarkin debe administrar las asignaciones de vehículos y Stromtroopers a las distintas misiones que parten desde la 
estrella de la muerte, para facilitar esta tarea nos encomienda desarrollar las funciones necesarias para gestionar esto mediante prioridades de la siguiente manera:
- de cada misión se conoce su tipo (exploración, contención o ataque), planeta destino y general que la solicitó;
- si la misión fue pedida por Palpatine o Darth Vader su prioridad será baja;
- si la misión es de prioridad alta los recursos se asignarán manualmente independientemente de su tipo;
- si la misión es de baja prioridad se asignarán los recursos de la siguiente manera dependiendo de su tipo:
   * exploración: 15 Scout Troopers y 2 speeder bike, 
   * contención: 30 Stormtroopers y tres vehículos aleatorios (AT-AT, AT-RT, AT-TE, AT-DP, AT-ST) pueden ser repetidos,
   * ataque: 50 Stormtroopers y siete vehículos aleatorios (a los anteriores se le suman AT-M6, AT-MP, AT-DT)
- realizar la atención de todas las misiones y mostrar los recursos asignados a cada una, permitiendo agregar nuevos pedidos de misiones durante la atención;
- indicar la cantidad total de recursos asignados a las misiones.
"""


import random


class Vehiculo:
    def __init__(self, tipo):
        self.tipo = tipo


class Stormtrooper:
    def __init__(self, tipo):
        self.tipo = tipo


class Mision:
    def __init__(self, tipo, destino, general, prioridad):
        self.tipo = tipo
        self.destino = destino
        self.general = general
        self.prioridad = prioridad if general not in ['Palpatine', 'Darth Vader'] else 'baja'
        self.vehiculos = []
        self.stormtroopers = []


class EstrellaMuerte:
    def __init__(self):
        self.misiones = []
        self.vehiculos = [Vehiculo(tipo) for tipo in ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"] for _ in range(50)]
        self.stormtroopers = [Stormtrooper('Scout Trooper') for _ in range(200)] + [Stormtrooper('Stormtrooper') for _ in range(2000)]
    
    def agregar_mision(self, mision):
        self.misiones.append(mision)
    
    def asignar_recursos(self):
        for mision in self.misiones:
            if mision.prioridad == 'alta':
                continue
            if mision.tipo == 'exploracion':
                mision.stormtroopers = [self.stormtroopers.pop(self.stormtroopers.index(st)) for st in self.stormtroopers if st.tipo == 'Scout Trooper'][:15]
                mision.vehiculos = [self.vehiculos.pop(self.vehiculos.index(vh)) for vh in self.vehiculos if vh.tipo == 'speeder bike'][:2]
            elif mision.tipo == 'contencion':
                mision.stormtroopers = [self.stormtroopers.pop(self.stormtroopers.index(st)) for st in self.stormtroopers if st.tipo == 'Stormtrooper'][:30]
                mision.vehiculos = random.sample(self.vehiculos, 3)
                for vh in mision.vehiculos:
                    self.vehiculos.remove(vh)
            elif mision.tipo == 'ataque':
                mision.stormtroopers = [self.stormtroopers.pop(self.stormtroopers.index(st)) for st in self.stormtroopers if st.tipo == 'Stormtrooper'][:50]
                mision.vehiculos = random.sample(self.vehiculos, 7)
                for vh in mision.vehiculos:
                    self.vehiculos.remove(vh)

    def mostrar_recursos_misiones(self):
        for mision in self.misiones:
            print(f"Misión {mision.tipo} a {mision.destino} solicitada por {mision.general} con prioridad {mision.prioridad}.")
            print(f"Asignados {len(mision.stormtroopers)} stormtroopers y {len(mision.vehiculos)} vehiculos.")
            print("Vehiculos asignados:")
            for vehiculo in mision.vehiculos:
                print(f"- {vehiculo.tipo}")
            print()

    def recursos_totales_asignados(self):
        total_stormtroopers = sum([len(mision.stormtroopers) for mision in self.misiones])
        total_vehiculos = sum([len(mision.vehiculos) for mision in self.misiones])
        print(f"Total de stormtroopers asignados: {total_stormtroopers}")
        print(f"Total de vehículos asignados: {total_vehiculos}")


# Crear una instancia de la Estrella de la Muerte
estrella_muerte = EstrellaMuerte()

# Crear algunas misiones
mision1 = Mision("exploracion", "Tatooine", "General Veers", "alta")
mision2 = Mision("contencion", "Hoth", "Darth Vader", "media")
mision3 = Mision("ataque", "Endor", "Palpatine", "baja")

# Agregar las misiones a la Estrella de la Muerte
estrella_muerte.agregar_mision(mision1)
estrella_muerte.agregar_mision(mision2)
estrella_muerte.agregar_mision(mision3)

# Asignar recursos a las misiones
estrella_muerte.asignar_recursos()

# Mostrar los recursos asignados a cada misión
estrella_muerte.mostrar_recursos_misiones()

# Mostrar el total de recursos asignados
estrella_muerte.recursos_totales_asignados()
