from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
import wikipedia
from django.contrib.auth.decorators import login_required
from .models import SavedSearch

# Create your views here.
@login_required(login_url='')
def wiki(request):
    if request.method == "POST":
        search = request.POST['search']
        try:
            result = wikipedia.summary(search, sentences=30)
        except:
            return HttpResponse("Wrong Input")
        return render(request, "main/index.html", {"result": result})
    return render(request, "main/index.html")

@login_required(login_url='')
def save_search(request):
    if request.method == "POST":
        query = request.POST['query']
        result = request.POST['result']
        user = request.user
        SavedSearch.objects.create(query=query, result=result, user=user)
        return redirect('archives')

@login_required(login_url='')
def archives(request):
    searches = SavedSearch.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "main/archives.html", {"searches": searches})