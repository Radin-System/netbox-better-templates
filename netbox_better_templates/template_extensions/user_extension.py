def user_extension(context):
    """
    Adds the `authenticated_user` object to the Jinja2 template context.
    """
    request = context.get('request')
    if request and hasattr(request, 'user'):
        return {
            'authenticated_user': request.user,
        }
    return {}