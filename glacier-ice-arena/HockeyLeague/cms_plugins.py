from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cms.models.pluginmodel import CMSPlugin

from . import models

class LeaguePlugin(CMSPluginBase):
    model = models.LeaguePlugin
    name = 'Hockey League Plugin'
    render_template = "hockey_league.html"

    def render(self, context, instance, placeholder):
        context = super(LeaguePlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(LeaguePlugin)
