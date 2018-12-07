from django.shortcuts import render
from .forms import Note
from random import randrange as rand

# Create your views here.

class Valeur:
	def __init__(self,matiere, note):
		self.note = note
		self.matiere = matiere

def noteGigi(request):
	if request.method == 'POST':
		form = Note(request.POST)
		if form.is_valid():
			maths = form.cleaned_data['maths']
			spe = form.cleaned_data['spe']
			physique = form.cleaned_data['physique']
			francais = form.cleaned_data['francais']
			notes = [maths, spe, physique, francais]
			result = []
			for note in notes:
				if rand(1000) != 0:
					note = rand(note)
				result.append(note)
			maths = Valeur("Maths",result[0])
			spe = Valeur("SVT/SI",result[1])
			physique = Valeur("Physique",result[2])
			fr = Valeur("Français",result[3])
			
			
			return render(request,'notes/result.html',{'notes':[maths, spe, physique, fr]})
			
	else:
		form = Note()
		
	return render(request, 'notes/notes_gigi.html',{'form': form})