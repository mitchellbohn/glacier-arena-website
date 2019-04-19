from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from . import models

class SchedulePlugin(CMSPluginBase):
    model = models.ScheduleGroup
    name = 'Schedule Plugin'
    render_template = "schedule_plugin.html"
    allow_children = True
    cache = False
    child_classes = ['SingleSchedule']

class SingleSchedule(CMSPluginBase):
    model = models.Schedule
    name = 'Schedule Entry'
    render_template = "schedule.html"
    require_parent = True
    cache = False
    parent_classes = ['SchedulePlugin']

plugin_pool.register_plugin(SchedulePlugin)
plugin_pool.register_plugin(SingleSchedule)