from importlib import import_module


def import_form_class(module):
    module = module.split(".")
    class_name = module.pop(-1)
    module = '.'.join(module)

    try:
        module = import_module(module)
        return getattr(module, class_name)
    except ImportError, e:
        raise ImportError(e.message)
    except AttributeError, e:
        raise AttributeError(e.message)


def get_object_or_none(klass, *args, **kwargs):
    """
    Uses get() to return an object, or raises a Http404 exception if the object
    does not exist.

    klass may be a Model. All other passed arguments and keyword arguments are used in the get() query.

    Note: Like with get(), an MultipleObjectsReturned will be raised if more than one
    object is found.
    """
    queryset = klass.objects
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None