from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.template import RequestContext
from presentation.forms import SeleccionUnicaForm


# Create your views here.
def presentation(request):
    if request.method == "POST":
        form = SeleccionUnicaForm(request.POST)
        if form.is_valid():
                form.save()
    else:
        form = SeleccionUnicaForm()
    
    if request.user.username == "admin":
        return render(request,'presentation_master.html', {'respuesta':form})
    else:
        return render(request,'presentation.html', {'respuesta':form})

