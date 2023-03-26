from django.shortcuts import HttpResponse
import wikipedia
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


# Create your views here.
def logout(request):
    return render(request, 'logout.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Kullanıcı adı veya şifre yanlış, formu hatalı göster.
            return render(request, 'login.html', {'error_message': 'Kullanıcı adı veya şifre yanlış.'})
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})


def home(request):
    if request.method == "POST":
        search = request.POST['search']
        try:
            result = wikipedia.summary(search, sentences=30)
        except:
            return HttpResponse("Wrong Input")
        return render(request, "main/index.html", {"result": result})
    return render(request, "main/index.html")
