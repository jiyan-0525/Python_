def ft_filter(func, iterable):
    """
    This function takes a function and an iterable as arguments and 
    returns a new iterable containing only the elements for which 
    the function returns True.
    """
    if func is None:
        return [item for item in iterable if item]
    return [item for item in iterable if func(item)]
