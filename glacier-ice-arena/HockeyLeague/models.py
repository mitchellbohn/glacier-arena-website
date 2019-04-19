from django.db import models
from cms.models import CMSPlugin

# Create your models here.

class League(CMSPlugin):
    League_Name = models.CharField(blank=True, max_length=200,)

class Team(models.Model):
    league = models.ForeignKey(League)
    name = models.CharField(blank = True, max_length=200,)
    team_logo = models.ImageField('Image Path')
    games_played = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    overtime_losses = models.IntegerField()
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()
    goal_difference = models.IntegerField()
    PTS = models.IntegerField()

class Player(models.Model):
    team = models.ForeignKey(Team)
    name = models.CharField(blank=True, max_length=200,)
    number = models.IntegerField()
    position = models.CharField(max_length=100,)

class Games(models.Model):
    league = models.ForeignKey(League)
    team1 = models.ForeignKey(Team)
    team2 = models.ForeignKey(Team)
    game_date = models.DateField(auto_now=False,)
    was_tie = models.BooleanField(default=False)
    was_overtime = models.BooleanField(default=False)
    team1_win = models.BooleanField(default=False)
    team1_goals = models.IntegerField()
    team2_win = models.BooleanField(default=False)
    team2_goals = models.IntegerField()