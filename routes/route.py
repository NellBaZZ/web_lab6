from flask import request, Blueprint
#from app import app
from flask import Flask
from flask_swagger import swagger
from controllers.clientsController import *
from controllers.publicationsConroller import *
from controllers.deliveryController import *
from controllers.purchaseController import *
from controllers.reviewsController import *
import json

routes = Blueprint('routes', __name__)

app = Flask(__name__)

# region swagger_json.txt
def generate_swagger_spec():
    # Создаем пустую спецификацию
    spec = {
        "openapi": "3.0.0",
        "info": {
            "version": "3.0.0",
            "title": "WebPurchasePublications",
        },
        "servers": [{"url": "/"}],
        "paths": {},
        "components": {}
    }

    # Добавляем маршруты клиентов
    spec["paths"]["/clients"] = {
        "post": {
            "summary": "Create a client",
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "fio": {"type": "string"},
                                "address": {"type": "string"}
                            },
                            "required": ["fio", "address"]
                        }
                    }
                }
            },
            "responses": {"200": {"description": "Client created"}}
        },
        "get": {
            "summary": "Get all clients",
            "responses": {"200": {"description": "List of clients"}}
        },
        "put": {
            "summary": "Update client",
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "integer"},
                                "fio": {"type": "string"},
                                "address": {"type": "string"}
                            }
                        }
                    }
                }
            },
            "responses": {"200": {"description": "Client updated"}}
        },
        "delete": {
            "summary": "Delete client",
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "integer"}
                            }
                        }
                    }
                }
            },"responses": {"200": {"description": "Review deleted"}}
        }
    }

    # Добавляем маршруты отзывов
    spec["paths"]["/reviews"] = {
        "post": {
            "summary": "Create a review",
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "client_id": {"type": "integer"},
                                "delivery_id": {"type": "integer"},
                                "grade": {"type": "integer"},
                                "text": {"type": "string"}
                            },
                            "required": ["client_id", "delivery_id", "grade"]
                        }
                    }
                }
            },
            "responses": {"200": {"description": "Review created"}}
        },
        "get": {
            "summary": "Get all reviews",
            "responses": {"200": {"description": "List of reviews"}}
        },
        "put": {
            "summary": "Update a review",
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "integer"},
                                "grade": {"type": "integer"},
                                "text": {"type": "string"}
                            }
                        }
                    }
                }
            },
            "responses": {"200": {"description": "Review updated"}}
        },
        "delete": {
            "summary": "Delete a review",
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "integer"}
                            }
                        }
                    }
                }
            },"responses": {"200": {"description": "Review deleted"}}
        }
    }
    return spec

@routes.route('/swagger_json')
def get_file_content():
    spec = generate_swagger_spec()
    return jsonify(spec)
# endregion swagger_json.txt

# region client routes
@routes.route('/clients', methods=['POST'])
def create_client_route():
    data = request.json
    fio = data.get('fio')
    address = data.get('address')
    return create_client(fio, address)

@routes.route('/clients', methods=['GET'])
def read_all_clients_route():
    return read_all_clients()

@routes.route('/clients', methods=['PUT'])
def update_client_route():
    data = request.json
    id = data.get('id')
    fio = data.get('fio')
    address = data.get('address')
    return update_client(id, fio, address)

@routes.route('/clients', methods=['DELETE'])
def delete_client_route():
    data = request.json
    id= data.get('id')
    return delete_client(id)
# endregion client

# region publications routes

@routes.route('/publications', methods=['POST'])
def create_publication_route():
    data = request.json
    id_type = data.get('id_type')
    name = data.get('name')
    price = data.get('price')
    return create_publication(id_type, name, price)

@routes.route('/publications', methods=['GET'])
def read_all_publications_route():
    return read_all_publications()

@routes.route('/publications', methods=['PUT'])
def update_publication_route(id):
    data = request.json
    id = data.get('id')
    id_type = data.get('id_type')
    name = data.get('name')
    price = data.get('price')
    return update_publication(id, id_type, name, price)

@routes.route('/publications', methods=['DELETE'])
def delete_publication_route(id):
    data = request.json
    id = data.get('id')
    return delete_publication(id)

# Routes for Type of Publication
@routes.route('/types-publication', methods=['POST'])
def create_type_publication_route():
    data = request.json
    tip = data.get('tip')
    return create_type_publication(tip)

@routes.route('/types-publication', methods=['GET'])
def read_all_types_publication_route():
    return read_all_types_publication()

@routes.route('/types-publication', methods=['PUT'])
def update_type_publication_route(id):
    data = request.json
    id = data.get('id')
    tip = data.get('tip')
    return update_type_publication(id, tip)

@routes.route('/types-publication', methods=['DELETE'])
def delete_type_publication_route(id):
    data = request.json
    id = data.get('id')
    return delete_type_publication(id)

# endregion publications routes

# region delivery routes

@routes.route('/couriers', methods=['POST'])
def create_courier_route():
    data = request.json
    fio = data.get('fio')
    return create_courier(fio)

@routes.route('/couriers', methods=['GET'])
def read_all_couriers_route():
    return read_all_couriers()

@routes.route('/couriers', methods=['PUT'])
def update_courier_route(id):
    data = request.json
    id = data.get('id')
    fio = data.get('fio')
    return update_courier(id, fio)

@routes.route('/couriers/<int:id>', methods=['DELETE'])
def delete_courier_route(id):
    data = request.json
    id = data.get('id')
    return delete_courier(id)


@routes.route('/deliveries', methods=['POST'])
def create_delivery_route():
    data = request.json
    id_courier = data.get('id_courier')
    name = data.get('name')
    return create_delivery(id_courier, name)

@routes.route('/deliveries', methods=['GET'])
def read_all_deliveries_route():
    return read_all_deliveries()

@routes.route('/deliveries', methods=['PUT'])
def update_delivery_route(id):
    data = request.json
    id = data.get('id')
    id_courier = data.get('id_courier')
    name = data.get('name')
    return update_delivery(id, id_courier, name)

@routes.route('/deliveries', methods=['DELETE'])
def delete_delivery_route(id):
    data = request.json
    id = data.get('id')
    return delete_delivery(id)

# endregion delivery routes

# region purchase routes

@routes.route('/purchases', methods=['POST'])
def create_purchase_route():
    data = request.json
    id_publication = data.get('id_publication')
    id_client = data.get('id_client')
    id_delivery = data.get('id_delivery')
    return create_purchase(id_publication, id_client, id_delivery)

@routes.route('/purchases', methods=['GET'])
def read_all_purchases_route():
    return read_all_purchases()

@routes.route('/purchases', methods=['DELETE'])
def delete_purchase_route(id):
    data = request.json
    id = data.get("id")
    return delete_purchase(id)

# endregion purchase routes

# region review routes

@routes.route('/reviews', methods=['POST'])
def create_review_route():
    data = request.json
    client_id = data.get('client_id')
    delivery_id = data.get('delivery_id')
    grade = data.get('grade')
    text = data.get('text')
    return create_review(client_id, delivery_id, grade, text)

@routes.route('/reviews', methods=['GET'])
def read_all_reviews_route():
    #data = request.json
   # id = data.get('id_delivery')
    return read_all_reviews()

@routes.route('/reviews', methods=['PUT'])
def update_review_route():
    data = request.json
    id = data.get('id')
    grade = data.get('grade')
    text = data.get('text')
    return update_review(id, grade, text)

@routes.route('/reviews', methods=['DELETE'])
def delete_review_route():
    data = request.json
    id = data.get('id')
    return delete_review(id)

# endregion review routes