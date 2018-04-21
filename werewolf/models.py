from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Character(models.Model):
    name = models.CharField('Name', max_length = 50)
    action = models.TextField('Action')
    priority = models.FloatField('Priority')

class Game(models.Model):
    OPEN = 'OP'
    CHARACTER_ASS = 'AS'
    CHARACTER_VIEW = 'VI'
    NIGHT = 'NI'
    DAY = 'DI'
    CLOSED = 'CL'
    GAME_STATE_CHOICES = (
        (OPEN, 'Open Membership'),
        (CHARACTER_ASS, 'Character Assignment'),
        (CHARACTER_VIEW, 'Character Viewing'),
        (NIGHT, 'Night Phase'),
        (DAY, 'Day Phase'),
        (CLOSED, 'Game Over'),
    )
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    created_on = models.DateTimeField('Created On', auto_now_add = True)
    game_key = models.CharField('Game Key', max_length = 15)
    state = models.CharField('Game State', max_length = 2, choices = GAME_STATE_CHOICES, default = OPEN)
    night_sub_state = models.ForeignKey('GameMembership', on_delete = models.CASCADE, null = True, blank = True, default = None)

class GameMembership(models.Model):
    game_key = models.ForeignKey(Game, on_delete = models.CASCADE)
    member = models.ForeignKey(User, on_delete = models.CASCADE)
    init_character = models.ForeignKey(Character, on_delete = models.CASCADE, null = True, blank = True, default = None)
    cur_character = models.ForeignKey(Character, on_delete = models.CASCADE, related_name = '+', null = True, blank = True, default = None)
    vote = models.ForeignKey('self', on_delete = models.CASCADE, null = True, blank = True, default = None)
