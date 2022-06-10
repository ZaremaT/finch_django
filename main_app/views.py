
from django.views.generic.base import TemplateView
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


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
        context["cats"] = Cat.objects.all()
        return context

class CatCreate(CreateView):
        model = Cat
        fields = ['breed', 'img', 'description', 'verified_cat']
        template_name = "cat_create.html"
        success_url = "/cats/"
        
class CatDetail(DetailView):
        model = Cat
        template_name = "cat_detail.html"   

class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'img', 'description', 'verified_cat']
    template_name = "cat_create.html"
    success_url = "/cats/"
    
class CatDelete(DeleteView):
    model = Cat
    template_name = "cat_delete.html"
    success_url = "/cats/"