class Observable:
    def __init__(self):
        self._observadores = []

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def eliminar_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)


class Observador:
    def actualizar(self, mensaje):
        pass


class ObservadorConcreto(Observador):
    def actualizar(self, mensaje):
        print("Observador recibió el mensaje:", mensaje)


# Uso del patrón Observable
observable = Observable()
observador1 = ObservadorConcreto()
observador2 = ObservadorConcreto()
observador3 = ObservadorConcreto()

# Registro de Observadores
observable.agregar_observador(observador1)
observable.agregar_observador(observador2)
observable.agregar_observador(observador3)

# Notificación a los Observadores
observable.notificar_observadores("¡Hola, mundo!")

# Elimina un observador
observable.eliminar_observador(observador3)

# Notificación a los observadores despues de elimnar 1
observable.notificar_observadores("¡Hola mundo de nuevo!")
