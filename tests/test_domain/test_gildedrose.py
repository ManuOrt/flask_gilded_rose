from domain.Backstage import Backstage
from domain.GildedRose import GildedRose
from domain.AgedBrie import AgedBrie
from domain.ConjuredItem import ConjuredItem
from domain.NormalItem import NormalItem
from domain.Sulfuras import Sulfuras


def test_gilded_rose():
    items = [NormalItem("Normal Varita sin magia", 9, 9, "normal"),
             ConjuredItem("Conjured Varita", 18, 4, "conjured"),
             AgedBrie("Aged Brie", 42, -1, "Agedbrie"),
             Sulfuras("Sulfuras", 80, 0),
             Backstage("Backstage", 26, 14, "backstage")]
    assert items[0].quality == 9
    assert items[0].sell_in == 9
    assert items[1].quality == 4
    assert items[1].sell_in == 18
    assert items[2].quality == -1
    assert items[2].sell_in == 42
    assert items[3].quality == 0
    assert items[3].sell_in == 80
    assert items[4].quality == 14
    assert items[4].sell_in == 26


def test_create_normal_item():
    baston = GildedRose.create_item("1231321", 'Normal Bastón', 10, 10, "normal")

    baston.update_quality()
    assert baston.name == 'Normal Bastón'
    assert baston.sell_in == 10
    assert baston.quality == 9


def test_create_aged_brie():
    queso = GildedRose.create_item("1234", 'Aged Brie Asturiano', 10, 10, "Agedbrie")

    queso.update_quality()
    assert queso.quality == 11
    assert queso.sell_in == 9


def test_create_conjured():
    varita = GildedRose.create_item("121212", 'Conjured varita', 10, 10, "conjured")

    varita.update_quality()

    assert varita.quality == 8
    assert varita.sell_in == 9