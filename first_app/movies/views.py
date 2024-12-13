from django.shortcuts import render
from django.http import HttpResponse

movie_list = [
    {
        "id": 1,
        "title": "The Witcher: Sword of Destiny",
        "author": "Andrzej Sapkowski",
    },
    {
        "id": 2,
        "title": "The Queens Gambit",
        "author": "Walter Tevis",
    },
    {
        "id": 3,
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
    },
]

# Create your views here.
def movies(request):
    http = "<h1>Movies</h1>"

    http += "<ul>"

    for movie in movie_list:
        http += f"<li>{movie['title']}</li>"
    
    http += "</ul>"

    return HttpResponse(http)

def movieDetails(request, id):
    targetMovie = {"id": 0, "title": "", "author": ""}

    for movie in movie_list:
        if (movie["id"] == int(id)):
            targetMovie = movie
            break

    return HttpResponse(f"<h1>Movie ID - {targetMovie['id']}</h1><h2>Title: {targetMovie['title']}</h2><h2>Author: {targetMovie['author']}</h2>")