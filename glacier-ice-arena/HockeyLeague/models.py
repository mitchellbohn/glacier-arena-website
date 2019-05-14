from django.db import models
from cms.models import CMSPlugin
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

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
    players = models.ManyToManyField(User, through='Player')

    def __str__(self):
        return self.name

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.pk))

class Player(models.Model):
    user = models.ForeignKey(User)
    team = models.ForeignKey(Team)
    name = models.CharField(blank=True, max_length=200,)
    number = models.IntegerField(null=True, blank=True,)
    position = models.CharField(null=True, blank=True, max_length=100,)

class Game(models.Model):
    league = models.ForeignKey(League)
    team1 = models.ForeignKey(Team, related_name="home")
    team2 = models.ForeignKey(Team, related_name="guest")
    game_date = models.DateField(auto_now=False,)
    was_tie = models.BooleanField(default=False)
    was_overtime = models.BooleanField(default=False)
    team1_win = models.BooleanField(default=False)
    team1_goals = models.IntegerField(default=0)
    team2_win = models.BooleanField(default=False)
    team2_goals = models.IntegerField(default=0)

class LeaguePlugin(CMSPlugin):
    league = models.ForeignKey(League)