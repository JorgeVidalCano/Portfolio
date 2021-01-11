from django.views.generic import(TemplateView)
from django.shortcuts import render
from .models import HomeData, AboutData

class Home(TemplateView):
    template_name = 'mainApp/home.html'
    model = HomeData

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        homedata = HomeData.objects.first()
        context.update({
            'tab': 'Home',
            'homedata': homedata,
        })
        return context
        
class About(TemplateView):
    template_name = 'mainApp/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aboutData = AboutData.objects.first()
        context.update({
            'tab': 'About',
            'aboutData': aboutData,
        })
        return context    

