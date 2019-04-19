from django.db import models
from cms.models import CMSPlugin

# Create your models here.

class ScheduleGroup(CMSPlugin):
    schedule_group_name = models.CharField(blank=True, max_length=200,)

    def __str__(self):
        return self.schedule_group_name

class Schedule(CMSPlugin):
    group = models.ForeignKey(ScheduleGroup, default=0)
    schedule_name = models.CharField(blank = True, max_length=200,)
    schedule_start_date = models.DateTimeField('Start Date')
    schedule_end_date = models.DateTimeField('End Date')
    schedule_file_name = models.FileField('File Path')

    def __str__(self):
        return self.schedule_name

