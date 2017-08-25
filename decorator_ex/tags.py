import functools


def enclosed(string, tag):
    return "<{tag}>{value}</{tag}>".format(tag=tag, value=string)


def add_tag(tag):
    def decorator(method):
        @functools.wraps(method)
        def f(*args, **kwargs):
            value = method(*args, **kwargs)
            return enclosed(string=value, tag=tag)
        return f
    return decorator
