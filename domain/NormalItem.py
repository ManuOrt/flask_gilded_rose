from domain.Item import Item
from domain.Interfaz import Interfaz


class NormalItem(Item, Interfaz):

    def __init__(self, name, sell_in, quality, type):
        Item.__init__(self, name, sell_in, quality, type)  # Utilizamos el constructor de Item.

    def setSell_in(self):  # La caducidad debe reducirse en 1 cada vez que se ejecute
        self.sell_in = self.sell_in - 1

    def setQuality(self, valor):
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)