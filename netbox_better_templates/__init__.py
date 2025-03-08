from netbox.plugins import PluginConfig

class NetboxBetterTemplatesConfig(PluginConfig):
    name = 'netbox_better_templates'
    verbose_name = 'Better Templates'
    description = 'Adds some functionality to NetBox templates and config render.'
    author = 'radin-system'
    author_email = 'technical@rsto.ir'
    version = '1.0.0'
    base_url = 'better-templates'

config = NetboxBetterTemplatesConfig