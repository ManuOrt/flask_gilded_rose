from domain.NormalItem import NormalItem


class ConjuredItem(NormalItem):

    def __init__(self, name, sell_in, quality, type):
        NormalItem.__init__(self, name, sell_in, quality, type)

    def update_quality(self):
        if self.sell_in >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSell_in()