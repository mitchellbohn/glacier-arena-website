from django.db import models
from cms.models import CMSPlugin

# Create your models here.

class League(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    league_name = models.CharField(max_length=100)

    def __str__(self):
        return self.league_name

class Team(models.Model):
    league = models.ForeignKey(League)
    name = models.CharField(blank = True, max_length=200,)
    team_logo = models.ImageField(upload_to="team-logos/")
    games_played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)
    overtime_losses = models.IntegerField(default=0)
    goals_for = models.IntegerField(default=0)
    goals_against = models.IntegerField(default=0)
    goal_difference = models.IntegerField(default=0)
    PTS = models.IntegerField(default=0)

class Player(models.Model):
    team = models.ForeignKey(Team)
    name = models.CharField(blank=True, max_length=200,)
    number = models.IntegerField()
    position = models.CharField(max_length=100,)

class Games(models.Model):
    league = models.ForeignKey(League)
    team1 = models.ForeignKey(Team, related_name="team1")
    team2 = models.ForeignKey(Team, related_name="team2")
    game_date = models.DateField(auto_now=False,)
    was_tie = models.BooleanField(default=False)
    was_overtime = models.BooleanField(default=False)
    team1_win = models.BooleanField(default=False)
    team1_goals = models.IntegerField(default=0)
    team2_win = models.BooleanField(default=False)
    team2_goals = models.IntegerField(default=0)

class LeaguePlugin(CMSPlugin):
    league = models.ForeignKey(League)