from rest_framework.views import exception_handler
from rest_framework.exceptions import NotFound, ValidationError
from custom_exceptions.custom_exceptions import NetworkError
from .exceptions_handlers.not_found_exception_handler import not_found_exception_handler
from .exceptions_handlers.validation_error_exception_handler import validation_error_exception_handler
from .exceptions_handlers.network_error_exception_handler import network_error_exception_handler

def custom_exceptions_handler(exc, context):

    if isinstance(exc, NotFound):
        return not_found_exception_handler(exc, context)

    if isinstance(exc, ValidationError) : 
        return validation_error_exception_handler(exc, context)
    
    if isinstance(exc, NetworkError) : 
        return network_error_exception_handler(exc, context)
    
    return exception_handler(exc, context)

