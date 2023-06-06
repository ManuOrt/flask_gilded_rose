from flask import Flask
from config import config
from models.entities.product import Product
from routes import product
from flask import send_file
from flask_cors import CORS

# ROUTES
app = Flask(__name__)
CORS(app)


def page_not_found(error):
    return "<h1>Page not found</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(product.main, url_prefix='/api')

    # Errors Handle
    app.register_error_handler(404, page_not_found)
    app.run(host='0.0.0.0', port=5000, debug=True)



## GET /items
## GET /items/<id>
## POST /items
## PUT /items/<id>
## DELETE /items/<id>