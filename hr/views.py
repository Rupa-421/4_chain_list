from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy


from .models import Person,State,District,City
from .forms import PersonForm


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')
#
#
class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('name')
    context = {'states': states}
    return render(request, 'hr/state_dropdown_list_options.html', context)

def load_districts(request):
    state_id = request.GET.get('state')
    districts = District.objects.filter(state_id=state_id).order_by('name')
    context = {'districts': districts}
    return render(request, 'hr/district_dropdown_list_options.html', context)

def load_cities(request):
    district_id = request.GET.get('district')
    cities = City.objects.filter(district_id=district_id).order_by('name')
    context = {'cities': cities}
    return render(request, 'hr/city_dropdown_list_options.html', context)