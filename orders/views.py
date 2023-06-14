#from core.users.models import Profile, User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from orders.models import City

# Create your views here.
class CityListView(ListView):
    model = City
    template_name = 'city_list.html'
    context_object_name = 'object_list'