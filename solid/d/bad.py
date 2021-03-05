class Manzano:
    manzanas = []

    def getManzanas(self):
        return self.manzanas


class ContadorDeManzanas:

    def __init__(self, manzano):
        """"""
        self.manzano = manzano()

    def cuantas(self):
        return len(self.manzano.getManzanas())
