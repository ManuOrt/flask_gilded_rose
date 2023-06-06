from domain.AgedBrie import AgedBrie
from domain.ConjuredItem import ConjuredItem
from domain.Backstage import Backstage
from domain.Sulfuras import Sulfuras
from domain.NormalItem import NormalItem
from db.db import get_connection
from domain.GildedRose import GildedRose


class Product:

    def __init__(self, id, name=None, sellin=None, quality=None, type=None) -> None:
        self.id = id
        self.name = name
        self.sellin = sellin
        self.quality = quality
        self.type = type

    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'sellin': self.sellin,
            'quality': self.quality,
            'type': self.type
        }


