from rx import create

# Definición de la clase Sujeto (Observable)
class SujetoNoticias:
    def __init__(self):
        self._ultima_noticia = None
        self.observable = create(self._publicar_noticias)

    def _publicar_noticias(self, observer, scheduler):
        def on_dispose():
            pass

        observer.on_next(self._ultima_noticia)
        return on_dispose

    def publicar_noticia(self, noticia):
        self._ultima_noticia = noticia
        self.observable.subscribe(lambda x: print(f"Noticia publicada: {x}"))


# Implementación Observador
class Suscriptor:
    def __init__(self, nombre):
        self.nombre = nombre

    def suscribirse(self, observable):
        observable.subscribe(lambda x: print(f'{self.nombre} ha recibido la noticia: "{x}"'))


# Uso del patrón Observer con la librería RxPY
sujeto_noticias = SujetoNoticias()

suscriptor1 = Suscriptor("Suscriptor 1")
suscriptor2 = Suscriptor("Suscriptor 2")

sujeto_noticias.publicar_noticia("¡Nueva noticia emocionante!")

# Suscripción de los observadores
sujeto_noticias.observable.subscribe(lambda x: print("Observador anónimo ha recibido la noticia:", x))
suscriptor1.suscribirse(sujeto_noticias.observable)
suscriptor2.suscribirse(sujeto_noticias.observable)

# Publicar otra noticia
sujeto_noticias.publicar_noticia("¡Otra noticia interesante!")
