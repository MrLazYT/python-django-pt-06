from django.shortcuts import render
from django.http import HttpResponse

movies = [
    {
        "title": "The Witcher: Sword of Destiny",
        "author": "Andrzej Sapkowski",
    },
    {
        "title": "The Queens Gambit",
        "author": "Walter Tevis",
    },
    {
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
    },
]

# Create your views here.
def movies(request):
    http = "<h1>Movies</h1>"

    http += "<ul>"

    for movie in movies:
        http += f"<li>{movie['title']}</li>"
    
    http += "</ul>"

    return HttpResponse(http)

def movieDetails(request, id):
    return HttpResponse(f"<h1>Movie ID - {id}</h1>")