class Item:

    def __init__(self, name, sell_in, quality, type):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.type = type

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

