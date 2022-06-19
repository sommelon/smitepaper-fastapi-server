def get_module(cls):
    """Return the module of the given class"""
    module = cls.__module__
    if module == "builtins":
        return ""
    return module


def get_fqn(cls):
    """Return the fully qualified name of the object."""
    module = get_module(cls)
    if not module:
        return cls.__qualname__  # avoid outputs like 'builtins.str'
    return module + "." + cls.__qualname__
