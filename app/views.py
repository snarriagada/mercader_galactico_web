from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .forms import CreateNewList
from django.forms import formset_factory
from .helpers import *

def index(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            print("INDEX", form.cleaned_data)
    else:
        form = CreateNewList()
    return render(request, 'app/index.html', {"form": form})

def questions(request):
    #mensaje = "Dato ingresado para I: %r" %request.GET["i"]
    if request.method == "POST":
        form_data = CreateNewList(request.POST)
        if form_data.is_valid():
            form_data = form_data.cleaned_data
            print("form data: ", form_data)
            # entregar form data a una funcion auxiliar
            try:
                conversion = set_conversion_data(form_data)
                metals_price = set_prices_data(form_data)
                output = handle_questions(form_data, conversion, metals_price)
            except Exception as e:
                output = ["ERROR: Los datos ingresados no siguen el formato indicado"]
    else:
        form_data = None

    return render(request, 'app/results.html',
     {"form_data": form_data, "output": output})

