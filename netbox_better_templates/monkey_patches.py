from datetime import datetime
from extras.models import ConfigTemplate


def patch_config_template_render() -> None:

    original_render = ConfigTemplate.render

    def new_render(self: ConfigTemplate, context = None):
        # Add datetime and user to the context
        new_context = context if context is not None else {}

        new_context.update(
            {
                'datetime': datetime,
                'now': datetime.now,
            },
        )
        return original_render(
            self, 
            context = new_context,
        )

    ConfigTemplate.render = new_render


__all__ = [
    'patch_config_template_render',
]