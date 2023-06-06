from domain.AgedBrie import AgedBrie
from domain.Backstage import Backstage
from domain.ConjuredItem import ConjuredItem
from domain.NormalItem import NormalItem
from domain.Sulfuras import Sulfuras


class GildedRose:

    @staticmethod
    def create_item(_id, name, sell_in, quality, item_type):
        item_types = {'normal': NormalItem, 'conjured': ConjuredItem, 'Agedbrie': AgedBrie, 'sulfuras': Sulfuras,
                      'Backstage': Backstage}
        item_class = item_types.get(item_type)
        if item_class:
            return item_class(name, sell_in, quality, item_type)
        else:
            raise ValueError(f"Tipo de item inválido {item_type}")

    @staticmethod
    def create_type(name, sellin, quality, item_type):
        if item_type == 'aged_brie':
            return AgedBrie(name, sellin, quality, item_type)
        if item_type == 'normal':
            return NormalItem(name, sellin, quality, item_type)
        if item_type == 'conjured':
            return ConjuredItem(name, sellin, quality)
        if item_type == 'sulfuras':
            return Sulfuras(name, sellin, quality)
        if item_type == 'back_stage':
            return Backstage(name, sellin, quality, item_type)
