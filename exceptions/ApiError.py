class ApiError(Exception):
    def __init__(self, status, message, errors = {}):
        self.status = status
        self.message = message
        self.errors = errors
        
        
    @staticmethod
    def bad_request(message = '', errors = {}):
        return ApiError(400, message, errors)
    
    @staticmethod
    def unauthorized_error():
        return ApiError(401, 'Нет авторизации!')