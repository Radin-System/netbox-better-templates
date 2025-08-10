from netbox.plugins import PluginMenuItem


menu_items = (
    PluginMenuItem(
        link='plugins:netbox_better_templates:readme',
        link_text='About',
        staff_only=True,
    ),
)