from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . import forms


def signin(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                redirect('home')
            else:
                message = 'Login failed!'
    return render(
        request, 'signin/signin.html', context={'form': form, 'message': message})
