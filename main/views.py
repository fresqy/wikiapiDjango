from django.shortcuts import render, HttpResponse
import wikipedia


# Create your views here.
def home(request):
    if request.method == "POST":
        search = request.POST['search']
        try:
            result = wikipedia.summary(search, sentences=3)
        except:
            return HttpResponse("Wrong Input")
        return render(request, "main/index.html", {"result": result})
    return render(request, "main/index.html")
