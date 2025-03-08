from datetime import datetime

def datetime_extension(context):
    """
    Adds the `datetime` module to the Jinja2 template context.
    """
    return {
        'datetime': datetime,
    }