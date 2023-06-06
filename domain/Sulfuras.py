from domain.Item import Item
from domain.NormalItem import NormalItem


class Sulfuras(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality, type)

    def update_quality(self):
        assert self.quality == 80, "quality de %s distinta de 80" % self.__class__.__name__
        pass
