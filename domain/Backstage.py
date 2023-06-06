from domain.Item import Item
from domain.NormalItem import NormalItem


class Backstage(NormalItem):

    def __init__(self, name, sell_in, quality, type):
        NormalItem.__init__(self, name, sell_in, quality, type)

    def setQuality(self, valor):
        NormalItem.setQuality(self, valor)

    def update_quality(self):
        if self.sell_in > 10:
            self.setQuality(1)
        elif self.sell_in > 5:
            self.setQuality(2)
        elif self.sell_in > 0:
            self.setQuality(3)
        else:
            self.quality = 0
        self.setSell_in()
