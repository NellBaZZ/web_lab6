# client_controller.py
from flask import jsonify
from models.model import Client

def create_client(fio, address):
    try:
        client = Client.create(fio=fio, address=address)
        return jsonify({'message': 'Client created successfully'}), 201
    except:
        return jsonify({'error': 'Failed to create client'}), 400

def read_all_clients():
    clients = Client.select()
    return jsonify([{'id': client.id, 'fio': client.fio, 'address': client.address} for client in clients])

def update_client(id, fio, address):
    try:
        client = Client.get(Client.id == id)
        client.fio = fio
        client.address = address
        client.save()
        return jsonify({'message': f'Client with id {id} updated successfully'})
    except Client.DoesNotExist:
        return jsonify({'error': 'Client not found'}), 404

def delete_client(id):
    try:
        client = Client.get(Client.id == id)
        client.delete_instance()
        return jsonify({'message': f'Client with id {id} deleted successfully'})
    except Client.DoesNotExist:
        return jsonify({'error': 'Client not found'}), 404
