from django.db import models
from cms.models import CMSPlugin

# Create your models here.

class League(CMSPlugin):
    League_Name = models.CharField(blank=True, max_length=200,)

class Team(models.Model):
    league = models.ForeignKey(League, related_name="associated_league")
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
    team = models.ForeignKey(Team, related_name="associated_team")
    name = models.CharField(blank=True, max_length=200,)
    number = models.IntegerField()
    position = models.CharField(max_length=100,)

class Games(models.Model):
    league = models.ForeignKey(League, related_name="associated_league")
    team1 = models.ForeignKey(Team, related_name="Team 1")
    team2 = models.ForeignKey(Team, related_name="Team 2")
    game_date = models.DateField(auto_now=False,)
    was_tie = models.BooleanField(default=False)
    was_overtime = models.BooleanField(default=False)
    team1_win = models.BooleanField(defualt=False)
    team1_goals = models.IntegerField()
    team2_win = models.BooleanField(defualt=False)
    team2_goals = models.IntegerField()