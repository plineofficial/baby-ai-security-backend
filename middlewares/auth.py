from functools import wraps
from flask import request

from exceptions.exception_handler import exception_handler
from exceptions.ApiError import ApiError

from utils.Token import Token

def auth_middleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            if not request.authorization:
                return exception_handler(ApiError.unauthorized_error())
            
            token = str(request.authorization).split()[1]
            tokenData = Token.validate_token(token)
            if not tokenData:
                return exception_handler(ApiError.unauthorized_error())
            
            request.user = {
                "user_id": tokenData['userId'],
                "email": tokenData['email']
            }
                
            return func(*args, **kwargs)
        
        except:
            return exception_handler(ApiError.unauthorized_error())
        
    return decorated_function