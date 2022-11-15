from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Baby, Toy
from .forms import FeedingForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'
def about(request):
  return render(request, 'about.html')
def babies_index(request):
  babies = Baby.objects.all()
  return render(request, 'Babies/index.html', { 'babies': babies })

def babies_detail(request, baby_id):
  baby = Baby.objects.get(id=baby_id)
  toys_baby_doesnt_have = Toy.objects.exclude(id__in = baby.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'babies/detail.html', { 
    'baby': baby, 'feeding_form': feeding_form, 'toys': toys_baby_doesnt_have
  })

class BabyCreate(CreateView):
  model = Baby
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

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

def assoc_toy(request, baby_id, toy_id):
  Baby.objects.get(id=baby_id).toys.add(toy_id)
  return redirect('babies_detail', baby_id=baby_id)

def signup(request):
  error_message = ""
  if request.method == "Post":
    pass
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)