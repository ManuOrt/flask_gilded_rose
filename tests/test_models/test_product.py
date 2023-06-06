from models.entities.product import Product


def test_product_to_JSON():
    # Create a Product object
    product = Product(id=1, name="Test Product", sellin=5, quality=10, type="normal")

    # Call the to_JSON() method
    product_json = product.to_JSON()

    # Check the result
    expected_json = {
        'id': 1,
        'name': 'Test Product',
        'sellin': 5,
        'quality': 10,
        'type': 'normal'
    }
    assert product_json == expected_json
