from rx import from_iterable, operators as ops


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
            observador.on_next(self._ultima_noticia)

    def publicar_noticia(self, noticia):
        self._ultima_noticia = noticia
        self.notificar_observadores()


class MiObserver:
    def on_next(self, noticia):
        print(f'Nueva noticia: {noticia}')

    def on_error(self, error):
        print(f'Error: {error}')    

    def on_completed(self):
        print('El flujo de noticias ha finalizado')


sujeto_noticias = SujetoNoticias()


noticias = [
    "Nueva noticia sobre Python",
    "Noticia sobre Java",
    "Otra noticia de Python",
    "Actualización sobre Django",
    "Artículo sobre Machine Learning en Python",
    "Última versión de TensorFlow lanzada"
]


observable_noticias = from_iterable(noticias).pipe(
    ops.filter(lambda noticia: 'python' in noticia.lower())
)


mi_observer = MiObserver()


observable_noticias.subscribe(mi_observer)
