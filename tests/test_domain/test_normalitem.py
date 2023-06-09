from domain.AgedBrie import AgedBrie
from domain.Backstage import Backstage
from domain.ConjuredItem import ConjuredItem
from domain.NormalItem import NormalItem
from domain.Sulfuras import Sulfuras


def test_normal_item():
    item = NormalItem("Normal Item", 10, 10, "normal")
    item.update_quality()
    item.setSell_in()
    assert item.quality == 9
    assert item.sell_in == 9
    item.update_quality()
    item.setSell_in()
    assert item.quality == 8
    assert item.sell_in == 8


def test_conjured_item():
    item = ConjuredItem("Conjured Item", 10, 10, "conjured")
    item.update_quality()
    assert item.quality == 8
    assert item.sell_in == 9
    item.update_quality()
    assert item.quality == 6
    assert item.sell_in == 8


def test_aged_brie():
    item = AgedBrie("Aged Brie", 10, 10, "Agedbrie")
    item.update_quality()
    assert item.quality == 11
    assert item.sell_in == 9
    item.quality = 50
    item.update_quality()
    assert item.quality == 50


def test_sulfuras():
    item = Sulfuras("Sulfuras", 10, 80)
    item.update_quality()
    assert item.quality == 80
    assert item.sell_in == 10


def test_backstage():
    item = Backstage("Backstage", 15, 10, "backstage")
    item.update_quality()
    assert item.quality == 11
    assert item.sell_in == 14
    item = Backstage("Backstage", 10, 10, "backstage")
    item.update_quality()
    assert item.quality == 12
    assert item.sell_in == 9
    item = Backstage("Backstage", 5, 10, "backstage")
    item.update_quality()
    assert item.quality == 13
    assert item.sell_in == 4
    item = Backstage("Backstage", 0, 10, "backstage")
    item.update_quality()