from django.shortcuts import render
from django.http import HttpResponse

users = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "example@mail.com"
    },
    {
        "id": 2,
        "name": "Semen Kos",
        "email": "semen.kos@mail.com"
    },
    {
        "id": 3,
        "name": "Petro Oles",
        "email": "petro.oles@mail.com"
    },
]

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello from Django!</h1>")

def list(request):

    html = "<h1>Users</h1>"
    html += "<ul>"
    
    for user in users:
        html += f"<li>{user['name']}</li>"
    
    html += "</ul>"

    return HttpResponse(html)

    return HttpResponse("<h1>Hello from Django!</h1>")

def details(request, id):
    return HttpResponse(f"User Details ID - {id}")

def about(request):
    return HttpResponse("<h1>About Page</h1>")