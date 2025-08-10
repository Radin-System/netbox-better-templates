import urllib
from datetime import datetime
from ..config_render_utils import RenderBuffer, raise_error


def patch_config_templates() -> None:
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
                'raise_error': raise_error,
            }
        )
        return original_render(
            self,
            context = new_context,
            queryset = queryset,
        )

    # Monkey patch
    ConfigTemplate.render = new_render

def patch_export_templates() -> None:
    from extras.models import ExportTemplate

    original_render = ExportTemplate.render

    def new_render(
            self: ExportTemplate, 
            context = None,
            queryset = None,
        ):
        new_context = context if context is not None else {}
        new_context.update(
            {
                'datetime': datetime,
                'now': datetime.now,
                'raise_error': raise_error,
            }
        )
        return original_render(
            self,
            context = new_context,
            queryset = queryset,
        )

    # Monkey patch
    ExportTemplate.render = new_render

def patch_custom_links() -> None:
    from extras.models import CustomLink

    original_render = CustomLink.render

    def new_render(
            self: CustomLink, 
            context,
        ):
        new_context = context if context is not None else {}
        new_context.update(
            {
                'urllib': urllib,
                'datetime': datetime,
                'now': datetime.now,
                'raise_error': raise_error,
            }
        )
        return original_render(
            self,
            context = new_context,
        )

    # Monkey patch
    CustomLink.render = new_render

__all__ = [
    'patch_config_templates',
    'patch_export_templates',
    'patch_custom_links',
]