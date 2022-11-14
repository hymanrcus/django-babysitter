from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Baby, Toy
from .forms import FeedingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
def babies_index(request):
  babies = Baby.objects.all()
  return render(request, 'Babies/index.html', { 'babies': babies })

def babies_detail(request, baby_id):
  baby = Baby.objects.get(id=baby_id)
  feeding_form = FeedingForm()
  return render(request, 'babies/detail.html', { 
    'baby': baby, 'feeding_form': feeding_form
  })

class BabyCreate(CreateView):
  model = Baby
  fields = '__all__'
class BabyUpdate(UpdateView):
  model = Baby
  fields = ['description', 'age']
class BabyDelete(DeleteView):
  model = Baby
  success_url = '/babies/'

  def add_feeding(request, baby_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
      new_feeding = form.save(commit=False)
      new_feeding.baby_id = baby_id
      new_feeding.save()
    return redirect('babies_detail', baby_id=baby_id)

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'