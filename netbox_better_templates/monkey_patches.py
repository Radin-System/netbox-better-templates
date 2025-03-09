from datetime import datetime
from extras.models import ConfigTemplate

original_render = ConfigTemplate.render

def new_render(self, context):
    # Add datetime and user to the context
    context.update({
        'datetime': datetime,
        'now': datetime.now,
    })
    return original_render(self, context)

ConfigTemplate.render = new_render