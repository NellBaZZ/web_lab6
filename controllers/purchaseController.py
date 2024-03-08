# purchase_controller.py
from flask import jsonify
from models.model import Purchase

def create_purchase(id_publication, id_client, id_delivery):
    try:
        purchase = Purchase.create(id_publication=id_publication, id_client=id_client, id_delivery=id_delivery)
        return jsonify({'message': 'Purchase created successfully'}), 201
    except:
        return jsonify({'error': 'Failed to create purchase'}), 400

def read_all_purchases():
    purchases = Purchase.select()
    return jsonify([{'id': purchase.id, 'id_publication': purchase.id_publication, 'id_client': purchase.id_client, 'id_delivery': purchase.id_delivery} for purchase in purchases])

def delete_purchase(id):
    try:
        purchase = Purchase.get(Purchase.id == id)
        purchase.delete_instance()
        return jsonify({'message': f'Purchase with id {id} deleted successfully'})
    except Purchase.DoesNotExist:
        return jsonify({'error': 'Purchase not found'}), 404
