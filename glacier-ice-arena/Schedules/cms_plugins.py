from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from . import models

@plugin_pool.register_plugin
class SchedulePlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "schedule_plugin.html"
    cache = False