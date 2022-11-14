from django.shortcuts import render
from .models import Baby


# class Baby:
#   def __init__(self, name, description, age):
#     self.name = name
#     self.description = description
#     self.age = age

# babies = [
#   Baby('Lolo', 'Kinda rude.', 3),
#   Baby('Sachi', 'Looks like a turtle.', 0),
#   Baby('Fancy', 'Happy fluff ball.', 4),
#   Baby('Bonk', 'Meows loudly.', 6)
# ]
    

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def babies_index(request):
  babies = Baby.objects.all()
  return render(request, 'babies/index.html', { 'babies': babies })

def babies_detail(request, baby_id):
  baby = Baby.objects.get(id=baby_id)
  return render(request, 'babies/detail.html', { 'baby': baby })