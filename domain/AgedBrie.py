from domain.NormalItem import NormalItem
from domain.Item import Item


class AgedBrie(NormalItem):

    def __init__(self, name, sellin, quality, type):
        Item.__init__(self, name, sellin, quality, type)

    def setQuality(self, valor):
        NormalItem.setQuality(self, valor)

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)

        self.setSell_in()

