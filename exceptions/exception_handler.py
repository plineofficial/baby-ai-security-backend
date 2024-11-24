from exceptions.ApiError import ApiError

def exception_handler(ex):
    
    if isinstance(ex, ApiError):
        return {
            'message': ex.message,
            'errors': ex.errors
        }, ex.status
        
    return {
        'message': "Ошибка, попробуйте еще раз!"
    }, 500