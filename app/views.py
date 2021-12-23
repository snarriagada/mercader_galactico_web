from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .forms import CreateNewList, CreateQuestions
from django.forms import formset_factory

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

        form_questions = CreateQuestions(request.POST)
        if form_questions.is_valid():
            print("Q ", form_questions.cleaned_data)
        
        form_data = CreateNewList(request.POST)
        if form_data.is_valid():
            form_data = form_data.cleaned_data
    else:
        form_questions = CreateQuestions()
        form_data = None

    return render(request, 'app/questions.html',
     {"form_questions": form_questions, "form_data": form_data})


def result_question(request):
    #mensaje = "Dato ingresado para I: %r" %request.GET["i"]
    if request.method == "POST":

        form_questions = CreateQuestions(request.POST)
        if form_questions.is_valid():
            print("Q ", form_questions.cleaned_data)

    else:
        form_questions = CreateQuestions()

    return render(request, 'app/results.html',
     {"form_questions": form_questions.cleaned_data})
