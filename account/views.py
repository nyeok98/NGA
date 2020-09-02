from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            photo_profil = form.cleaned_data.get('photo_profil')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password = raw_password)
            login(request, account)
            return redirect('main')
        else:
            context['registration_form'] = form
            
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('main')


def login_view(request):
    user = request.user

    if user.is_authenticated:
        return redirect("main")
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("main")

    else:
        form = AccountAuthenticationForm()
    
    context = dict()
    context['login_form'] = form
    return render(request, 'login.html', context)

        


