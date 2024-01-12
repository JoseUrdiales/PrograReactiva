# Definición de la clase Sujeto (Observable)
class SujetoNoticias:
    def __init__(self):
        self._observadores = []
        self._ultima_noticia = None

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def eliminar_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self._observadores:
            observador.actualizar(self._ultima_noticia)

    def publicar_noticia(self, noticia):
        self._ultima_noticia = noticia
        self.notificar_observadores()


# Definición de la clase Observador
class ObservadorNoticias:
    def actualizar(self, noticia):
        pass
