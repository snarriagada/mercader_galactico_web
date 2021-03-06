from django import forms

class CreateNewList(forms.Form):
    i = forms.CharField(label="I", required=False)
    v = forms.CharField(label="V", required=False)
    x = forms.CharField(label="X", required=False)
    l = forms.CharField(label="L", required=False)
    c = forms.CharField(label="C", required=False)
    d = forms.CharField(label="D", required=False)
    m = forms.CharField(label="M", required=False)
    gold = forms.CharField(label="Cantidad de Oro en creditos", required=False)
    silver = forms.CharField(label="Cantidad de Plata en creditos", required=False)
    iron = forms.CharField(label="Cantidad de Hierro en creditos", required=False)
    question = forms.CharField(label="Tus preguntas", widget=forms.Textarea)

'''
class CreateQuestions(forms.Form):
    CHOICES = (('Gold', 'Gold'),('Silver', 'Silver'),('Iron', 'Iron'))
    metal = forms.ChoiceField(choices=CHOICES, required=True)
    quantity = forms.CharField(label="Galactic quantity", required=True)

class Convert(forms.Form):
    quantity = forms.CharField(label="Galactic quantity", required=True)

class MetalPrices(forms.Form):
    CHOICES = (('Gold', 'Gold'),('Silver', 'Silver'),('Iron', 'Iron'))
    metal = forms.ChoiceField(choices=CHOICES, required=False)
    galactic_price = forms.CharField(label="Galactic price", required=False)
    credits_price = forms.IntegerField(label="Credits price", required=False)
'''


