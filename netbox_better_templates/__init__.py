from netbox.plugins import PluginConfig

class NetboxBetterTemplatesConfig(PluginConfig):
    name = 'netbox_better_templates'
    verbose_name = 'Better Templates'
    description = 'Adds new functionality to NetBox config templates.'
    author = 'radin-system'
    author_email = 'technical@rsto.ir'
    version = '1.0.1'
    base_url = 'better-templates'


    def ready(self):
        # Apply the monkey patch when the app is ready
        from . import monkey_patches

config = NetboxBetterTemplatesConfig