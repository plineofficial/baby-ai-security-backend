from flask import request

from model import model
from exceptions.exception_handler import exception_handler
from middlewares.auth import auth_middleware

def init(app):
    
    @app.route('/api/predict', methods=['POST'])
    @auth_middleware
    def predict():
        try:
            preprocessed_text = model.preprocess_text(request.json['text']) 
            
            category_id, category_label, confidence = model.predict(preprocessed_text)
            
            return {
                'category_id': category_id,
                'category_label': category_label,
                'confidence': confidence,
            }, 200

        except Exception as ex:
            return exception_handler(ex)