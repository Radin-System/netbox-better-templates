from django.apps import AppConfig

class BetterTemplatesAppConfig(AppConfig):
    name = 'netbox_better_templates'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        # Import and register template extensions
        from netbox_better_templates.template_extensions.datetime_extension import datetime_extension
        from netbox_better_templates.template_extensions.user_extension import user_extension
        from netbox.plugins import PluginConfig
        from netbox.registry import registry

        # Register template extensions
        registry['plugin_template_extensions']['netbox_better_templates'] = {
            'datetime': datetime_extension,
            'authenticated_user': user_extension,
        }