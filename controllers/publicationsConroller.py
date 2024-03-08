# publication_controller.py
from flask import jsonify
from models.model import Publication, TypePublication

# region publication
def create_publication(id_type, name, price):
    try:
        publication = Publication.create(id_type=id_type, name=name, price=price)
        return jsonify({'message': 'Publication created successfully'}), 201
    except:
        return jsonify({'error': 'Failed to create publication'}), 400

def read_all_publications():
    publications = Publication.select()
    return jsonify([{'id': publication.id, 'id_type': publication.id_type, 'name': publication.name, 'price': publication.price} for publication in publications])

def update_publication(id, id_type, name, price):
    try:
        publication = Publication.get(Publication.id == id)
        publication.id_type = id_type
        publication.name = name
        publication.price = price
        publication.save()
        return jsonify({'message': f'Publication with id {id} updated successfully'})
    except Publication.DoesNotExist:
        return jsonify({'error': 'Publication not found'}), 404

def delete_publication(id):
    try:
        publication = Publication.get(Publication.id == id)
        publication.delete_instance()
        return jsonify({'message': f'Publication with id {id} deleted successfully'})
    except Publication.DoesNotExist:
        return jsonify({'error': 'Publication not found'}), 404
# endregion publication

# region type

def create_type_publication(tip):
    try:
        type_publication = TypePublication.create(tip=tip)
        return jsonify({'message': 'Type of publication created successfully'}), 201
    except:
        return jsonify({'error': 'Failed to create type of publication'}), 400

def read_all_types_publication():
    types_publication = TypePublication.select()
    return jsonify([{'id': type_publication.id, 'tip': type_publication.tip} for type_publication in types_publication])

def update_type_publication(id, tip):
    try:
        type_publication = TypePublication.get(TypePublication.id == id)
        type_publication.tip = tip
        type_publication.save()
        return jsonify({'message': f'Type of publication with id {id} updated successfully'})
    except TypePublication.DoesNotExist:
        return jsonify({'error': 'Type of publication not found'}), 404

def delete_type_publication(id):
    try:
        type_publication = TypePublication.get(TypePublication.id == id)
        type_publication.delete_instance()
        return jsonify({'message': f'Type of publication with id {id} deleted successfully'})
    except TypePublication.DoesNotExist:
        return jsonify({'error': 'Type of publication not found'}), 404

# endregion type