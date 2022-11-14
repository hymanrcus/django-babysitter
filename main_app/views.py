from django.shortcuts import render
from django.http import HttpResponse


class Baby:
  def __init__(self, name, description, age):
    self.name = name
    self.description = description
    self.age = age

babies = [
  Baby('Lolo', 'Kinda rude.', 3),
  Baby('Sachi', 'Looks like a turtle.', 0),
  Baby('Fancy', 'Happy fluff ball.', 4),
  Baby('Bonk', 'Meows loudly.', 6)
]
    

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def babies_index(request):
  return render(request, 'babies/index.html', { 'babies': babies })