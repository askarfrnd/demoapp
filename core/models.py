from django.db import models


class Log(models.Model):
    name = models.CharField(max_length=255)
    timestamp_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
