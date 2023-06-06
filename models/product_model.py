from typing import List

from models.entities.product import Product
from db.db import get_connection
from domain.GildedRose import GildedRose


class ProductModel:

    @classmethod
    def get_products(self):
        try:
            connection = get_connection()
            products = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, sellin, quality, type FROM inventory ORDER BY name ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    product = Product(row[0], row[1], row[2], row[3], row[4])
                    products.append(product)

            connection.close()
            return products
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_product(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, sellin, quality, type FROM inventory WHERE id = %s", (id,))
                row = cursor.fetchone()

                product = None
                if row != None:
                    product = Product(row[0], row[1], row[2], row[3], row[4])

            connection.close()
            return product
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_product(self, product):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO inventory (id, name, sellin, quality, type)"
                               "VALUES (%s, %s, %s, %s, %s)",
                               (product.id, product.name, product.sellin, product.quality, product.type))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_product(self, product):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM inventory WHERE id = %s", (product.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_product(self, product):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE inventory SET name = %s, sellin = %s, quality = %s WHERE id = %s",
                               (product.name, product.sellin, product.quality, product.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_products(self, items):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                for item in items:
                    cursor.execute(
                        "UPDATE inventory SET sellin = %s, quality = %s WHERE id = %s",
                        (item.sell_in, item.quality, item.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
