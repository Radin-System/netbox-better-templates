from datetime import datetime
from ..config_render_utils import RenderBuffer


def patch_config_template_render() -> None:
    from extras.models import ConfigTemplate

    original_render = ConfigTemplate.render

    def new_render(
            self: ConfigTemplate, 
            context = None,
            queryset = None,
        ):
        new_context = context if context is not None else {}
        new_context.update(
            {
                'datetime': datetime,
                'now': datetime.now,
                'Buffer': RenderBuffer(),
            },
        )
        return original_render(
            self,
            context = new_context,
            queryset = queryset,
        )

    # Monkey patch
    ConfigTemplate.render = new_render


__all__ = [
    'patch_config_template_render',
]