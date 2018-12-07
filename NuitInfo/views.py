from django.shortcuts import render
from events.models import Event
from bde.models import Description
from annales.models import Annale

def index(request):
	events = Event.objects.order_by('-date')
	return render(request,'NuitInfo/index.html', {'events': events})
	
def bde(request):
	description = Description.objects.get(title = "L'équipe")
	return render(request, 'NuitInfo/bde.html', {'article': description})
	
def cpbx(request):
	description = Description.objects.get(title = "Le CPBx c'est quoi ?")
	return render(request, 'NuitInfo/cpbx.html', {'article': description})
	
def liens(request):
	annales = Annale.objects.all()
	return render(request, 'NuitInfo/liens.html', {'annales': annales})
	
def detente(request):
	return render(request,'NuitInfo/detente.html')