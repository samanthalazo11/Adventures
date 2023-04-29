from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Destination
from .forms import RestaurauntsForm, ExcursionsForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def destinations_index(request):
    destinations = Destination.objects.filter(user=request.user)
    return render(request, 'destinations/index.html', {'destinations':destinations})

@login_required
def destinations_detail(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    restauraunts_form = RestaurauntsForm()
    excursions_form = ExcursionsForm()
    return render(request, 'destinations/detail.html', {
        'destination':destination,
        'restauraunts_form':restauraunts_form,
        'excursions_form': excursions_form
         })

def add_restauraunts(request, destination_id):
    form = RestaurauntsForm(request.POST)
    if form.is_valid():
        new_restauraunts = form.save(commit=False)
        new_restauraunts.destination_id = destination_id
        new_restauraunts.save()

    return redirect('destinations_detail', destination_id=destination_id)

def add_excursions(request, destination_id):
    form = ExcursionsForm(request.POST)
    if form.is_valid():
        new_excursions = form.save(commit=False)
        new_excursions.destination_id = destination_id
        new_excursions.save()

    return redirect('destinations_detail', destination_id=destination_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('destinations_index')
        else:
            error_message = 'Not valid - try again'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error': error_message})

# class add_restaurauntsDelete(DeleteView):
#     model= add_restauraunts
#     success_url = '/destinations/'
#     template_name = 'destinations/destination_confirm_delete.html'


class DestinationCreate(LoginRequiredMixin, CreateView):
    model = Destination
    fields = ('location','budget','dates', 'flights', 'hotel', 'notes')
    template_name= 'destinations/destination_form.html'
    # success_url = '/destinations/'
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DestinationUpdate(LoginRequiredMixin, UpdateView):
    model = Destination
    fields = ('budget', 'flights', 'hotel', 'notes', 'dates')
    template_name= 'destinations/destination_form.html'

class DestinationDelete(LoginRequiredMixin, DeleteView):
    model= Destination
    success_url = '/destinations/'
    template_name = 'destinations/destination_confirm_delete.html'
