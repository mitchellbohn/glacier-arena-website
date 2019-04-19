from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cms.models.pluginmodel import CMSPlugin

from . import models

class LeaguePlugin(CMSPluginBase):
    model = models.League
    name = 'Hockey League Plugin'
    render_template = "league.html"
