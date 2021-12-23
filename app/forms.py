from django import forms

class CreateNewList(forms.Form):
    i = forms.IntegerField(label="I", required=False)
    v = forms.IntegerField(label="V", required=False)
    x = forms.IntegerField(label="X", required=False)
    l = forms.IntegerField(label="L", required=False)
    c = forms.IntegerField(label="C", required=False)
    d = forms.IntegerField(label="D", required=False)
    m = forms.IntegerField(label="M", required=False)
    gold = forms.CharField(label="Gold Conversion", required=False)
    silver = forms.CharField(label="Silver Conversion", required=False)
    iron = forms.CharField(label="Iron Conversion", required=False)

class CreateQuestions(forms.Form):
    question = forms.CharField(label="Your Questions", widget=forms.Textarea)
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


