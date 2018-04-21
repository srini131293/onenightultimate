from django.http import HttpResponse
from django.shortcuts import render

from werewolf.models import Character, Game, GameMembership

# Create your views here.
def index(request):
    return render(request, 'index.html')

def waitingforplayers(request):
    gameKey = request.GET['gameKey']
    try:
        game = Game.objects.get(game_key=gameKey)
    except Game.DoesNotExist:
        game = Game(game_key=gameKey, created_by=request.user)
        game.save()

    try:
        GameMembership.objects.get(game_key=game.id, member = request.user.id)
    except GameMembership.DoesNotExist:
        if game.state != Game.OPEN:
            raise Exception("Game Closed!")
        
        game_member = GameMembership(game_key=game, member=request.user)
        game_member.save()


    #  TODO: CHANGE THIS LATER!!!
    if game.state != Game.OPEN:
            raise Exception("Game Closed!")

    members = GameMembership.objects.filter(game_key = game.id)
    return render(request, 'waitingforplayers.html', {'gameKey' : gameKey, 'members' : members, 'game' : game})
