def raise_error(exception_name: str, message: str) -> None:
    exception_class = globals().get(exception_name, Exception)

    if issubclass(exception_class, Exception):
        raise exception_class(message)

    else:
        raise Exception(message)
