from .interfaces import ManzanoCountable


class Manzano(ManzanoCountable):
    manzanos = []

    def getMananos(self):
        """"""
        return self.manzanos


class CountMazanos:

    def __init__(self, mazano: ManzanoCountable):
        self.mazano = mazano

    def cuantas(self):
        return len(self.mazano.getMananos())
