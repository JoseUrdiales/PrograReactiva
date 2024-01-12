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


# Implementación concreta del Observador
class Suscriptor(ObservadorNoticias):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, noticia):
        print(f'{self.nombre} ha recibido la noticia: "{noticia}"')


# Uso del patrón Observer
sujeto_noticias = SujetoNoticias()

suscriptor1 = Suscriptor("Suscriptor 1")
suscriptor2 = Suscriptor("Suscriptor 2")

sujeto_noticias.agregar_observador(suscriptor1)
sujeto_noticias.agregar_observador(suscriptor2)

sujeto_noticias.publicar_noticia("¡Nueva noticia emocionante!")