from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.


class Home(TemplateView):
    template_name="home.html"
    


class About(TemplateView):
  template_name = "about.html"
  
  class Cat:
      def __init__(self, breed, image, description):
        self.breed = breed
        self.image = image
        self.description = description
        
        
        
class CatList(TemplateView):
    template_name = "cat_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cats"] = cats # this is where we add the key into our context object for the view to use
        return context