from netbox.plugins import PluginConfig
from .monkey_patches import patch_config_template_render
from ._version import get_version

class NetboxBetterTemplatesConfig(PluginConfig):
    name = 'netbox_better_templates'
    verbose_name = 'Better Templates'
    description = 'Adds new functionality to NetBox config templates.'
    author = 'radin-system'
    author_email = 'info@rsto.ir'
    version = get_version()
    base_url = 'better-templates'

    def ready(self):
        super().ready()

        patch_config_template_render()


    def __str__(self) -> str:
        return self.name

config = NetboxBetterTemplatesConfig