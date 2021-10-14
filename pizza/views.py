from django.shortcuts import render, redirect
from .forms import PizzaForm
# from .models import Pizza
# Create your views here.

def pizza_create(request):
    form = PizzaForm()
    if request.method == 'POST':
        form= PizzaForm(request.POST) 
        if form.is_valid(): #Check
            form.save()
            return redirect('home') 
    context = {'form': form}
    return render(request,'pizza/order.html', context)

def home(request):
    return render(request,'pizza/home.html' )
