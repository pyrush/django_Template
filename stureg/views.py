from django.shortcuts import render
from django.views.generic.base import View, TemplateView


class HomeView(TemplateView):
    template_name = "stureg/index.html"


class AboutView(TemplateView):
    template_name = "stureg/about.html"
