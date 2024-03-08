from flask import jsonify
from models.model import Delivery, Courier

#region courier
def create_courier(fio):
    try:
        courier = Courier.create(fio=fio)
        return jsonify({'message': 'Courier created successfully'}), 201
    except:
        return jsonify({'error': 'Failed to create courier'}), 400

def read_all_couriers():
    couriers = Courier.select()
    return jsonify([{'id': courier.id, 'fio': courier.fio} for courier in couriers])

def update_courier(id, fio):
    try:
        courier = Courier.get(Courier.id == id)
        courier.fio = fio
        courier.save()
        return jsonify({'message': f'Courier with id {id} updated successfully'})
    except Courier.DoesNotExist:
        return jsonify({'error': 'Courier not found'}), 404

def delete_courier(id):
    try:
        courier = Courier.get(Courier.id == id)
        courier.delete_instance()
        return jsonify({'message': f'Courier with id {id} deleted successfully'})
    except Courier.DoesNotExist:
        return jsonify({'error': 'Courier not found'}), 404
# endregion courier

# region delivery
def create_delivery(id_courier, name):
        try:
            delivery = Delivery.create(id_courier=id_courier, name=name)
            return jsonify({'message': 'Delivery created successfully'}), 201
        except:
            return jsonify({'error': 'Failed to create delivery'}), 400

def read_all_deliveries():
    deliveries = Delivery.select()
    return jsonify([{'id': delivery.id, 'id_courier': delivery.id_courier, 'name': delivery.name} for delivery in deliveries])

def update_delivery(id, id_courier, name):
    try:
        delivery = Delivery.get(Delivery.id == id)
        delivery.id_courier = id_courier
        delivery.name = name
        delivery.save()
        return jsonify({'message': f'Delivery with id {id} updated successfully'})
    except Delivery.DoesNotExist:
        return jsonify({'error': 'Delivery not found'}), 404

def delete_delivery(id):
    try:
        delivery = Delivery.get(Delivery.id == id)
        delivery.delete_instance()
        return jsonify({'message': f'Delivery with id {id} deleted successfully'})
    except Delivery.DoesNotExist:
        return jsonify({'error': 'Delivery not found'}), 404
# endregion delivery