from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies':['gladiator', 'Top gun', 'made up movie']
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html',{})


# app/templates/movies/index.html