from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate, logout

from .forms import SignUpForm

def signup (request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})

# Create your views here.
