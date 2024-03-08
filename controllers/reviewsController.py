# review_controller.py
from flask import jsonify
from models.model import Review


def create_review(client_id, delivery_id, grade, text=None):
    try:
        review = Review.create(id_client=client_id, id_delivery=delivery_id, grade=grade, text=text)
        return jsonify({'message': 'Review created successfully'}), 201
    except Exception as e:
        return jsonify({'error': f'Failed to create review: {e}'}), 400

def read_all_reviews():
    reviews = Review.select()
    review_list = [{'id': review.id, 'id_client': review.id_client.id, 'id_delivery': review.id_delivery.id, 'grade': review.grade, 'text': review.text} for review in reviews]
    return jsonify(review_list)

    #return jsonify([{'id': review.id, 'id_client': review.id_client, 'id_delivery': review.id_delivery, 'grade': review.grade, 'text': review.text} for review in reviews])

def update_review(id, grade, text=None):
    try:
        review = Review.get(Review.id == id)
        review.grade = grade
        review.text = text
        review.save()
        return jsonify({'message': f'Review with id {id} updated successfully'})
    except Review.DoesNotExist:
        return jsonify({'error': 'Review not found'}), 404

def delete_review(id):
    try:
        review = Review.get(Review.id == id)
        review.delete_instance()
        return jsonify({'message': f'Review with id {id} deleted successfully'})
    except Review.DoesNotExist:
        return jsonify({'error': 'Review not found'}), 404
