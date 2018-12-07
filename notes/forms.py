from django import forms

class Note(forms.Form):
	maths = forms.DecimalField(max_value=20, min_value=0)
	spe = forms.DecimalField(label = 'SVT/SI',max_value=20, min_value=0)
	physique = forms.DecimalField(max_value=20, min_value=0)
	francais = forms.DecimalField(label= 'Français', max_value=20, min_value=0)