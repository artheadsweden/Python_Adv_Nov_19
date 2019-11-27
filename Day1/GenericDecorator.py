def generic(f):
    """
     This decorator is a light version of singledispatch from functools.
     This shows how we can decorate one function and then use that functions
     name to register other functions that will be executed with a call to the
     function that was first called. In this case they be dispatch on
     their argument type.
     :param f: Original function to be decorated
     :return: Reference to function wrapper
     """
    regestry = {}
    def register(t, func=None):
        """
         When decorating with .register func will be None
         If that is the case we will return a lambda that will call register
         with a reference to the function decorated

         :param t: The type tp be registered
         :param func: Reference to the decorated function
         :return: A function reference
         """
        if func is None:
            return lambda fu: register(t, fu)
        regestry[t] = func
        return func

    def dispatch(t):
        """
          dispatch will return the correct function from the registry
          :param t: The type that was provided
          :return: a function
          """
        return regestry[t]

    def wrapper(*args, **kwargs):
        """
        Wrapper will just take care if calling the dispatch
        function with the right type.
        The dispatch function returns the right function to call
        so we do that and provide the *args and **kwargs for that function

        :param args: Positional args to original function
        :param kwargs: Keyword args to original function
        :return: Whatever the original function returns
        """
        t = args[0].__class__
        if t not in regestry:
            return f(*args, **kwargs)
        return dispatch(t)(*args, **kwargs)
    wrapper.register = register
    return wrapper


@generic
def func(arg, verbose=False):
    if verbose:
        print("Let me just say, ", end="")
    print(arg)


@func.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Strength in the numbers, ", end="")
    print(arg)


@func.register(list)
def _(arg, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, item in enumerate(arg):
        print(i, item)


def main():
    func(10, True)
    func("Hi", True)
    func([1, 2, 3], True)


if __name__ == '__main__':
    main()
