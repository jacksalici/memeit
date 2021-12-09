from django.shortcuts import render, redirect
from django.http import Http404

# Create your views here.


def index(request):
    if request.method == "POST":
        room_id = request.POST.get("room_id")
        char_choice = request.POST.get("character_choice")
        return redirect(
            '/play/%s?&choice=%s' 
            %(room_id, char_choice)
        )
    return render(request, "index.html", {})

def game(request, room_id):
    choice = request.GET.get("choice")
    if choice not in ['X', 'O']:
        raise Http404("Choice does not exists")
    context = {
        "char_choice": choice, 
        "room_id": room_id
    }
    return render(request, "game.html", context)