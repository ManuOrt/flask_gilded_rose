import pytest

from db.db import get_connection
from models.product_model import ProductModel
from models.entities.product import Product


def test_get_products():
    # Call the function
    products = ProductModel.get_products()

    # Check the result
    assert isinstance(products, list)
    assert len(products) > 0

    for product in products:
        assert isinstance(product, Product)


def test_get_product():
    # Insert a new product into the db
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO inventory (id, name, sellin, quality, type) VALUES (%s, %s, %s, %s, %s)",
                       ("54223412432", "Test Product", 5, 10, "normal"))
    connection.commit()

    # Retrieve the product and check that it matches the inserted data
    product = ProductModel.get_product("54223412432")
    assert product.id.strip() == "54223412432"
    assert product.name == "Test Product"
    assert product.sellin == 5
    assert product.quality == 10
    assert product.type == "normal"

    # Clean up by deleting the inserted product
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM inventory WHERE id = %s", ("54223412432",))
    connection.commit()
    connection.close()


