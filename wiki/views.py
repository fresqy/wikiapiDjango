from django.shortcuts import render
from django.shortcuts import HttpResponse
import wikipedia
from django.contrib.auth.decorators import login_required

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
