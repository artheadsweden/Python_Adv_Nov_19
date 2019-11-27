import inspect
from functools import wraps


def private(method):
    class_name = inspect.stack()[1][3]
    @wraps(method)
    def privatized_method(*args, **kwargs):
        call_frame = inspect.stack()[1][0]
        if 'self' in call_frame.f_locals:
            call_class_name = call_frame.f_locals['self'].__class__.__name__
            if class_name == call_class_name:
                return method(*args, **kwargs)
        raise TypeError("can't call private method")
    return privatized_method
