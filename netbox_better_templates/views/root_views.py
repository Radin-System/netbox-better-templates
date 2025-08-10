from django.views.generic import View
from django.shortcuts import render

class ReadMeView(View):
    template_name = 'netbox_better_templates/readme.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


__all__ = [
    'ReadMeView',
]