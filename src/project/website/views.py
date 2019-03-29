from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView


class MainView(TemplateView):
    template_name = 'index.html'
