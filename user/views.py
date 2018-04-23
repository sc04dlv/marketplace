from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


def login(request):
    args = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Invalid login or password"
    return render(request, 'user/login.html', args)

def register(request):
    args = {}
    args['form'] = CustomUserCreationForm()
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=form.cleaned_data["username"],
                                     password=form.cleaned_data["password2"])
            auth.login(request, user)
            return redirect('/')
        else:
            args['form'] = form
    return render(request, 'user/register.html', args)

def logout(request):
  auth.logout(request)
  return redirect('/')
