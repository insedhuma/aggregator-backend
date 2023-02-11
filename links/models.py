from django.db import models
from core.models import TimestampedModel
from django.conf import settings

class Link(TimestampedModel):
    
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    url = models.URLField()
    description = models.TextField()
class Vote(TimestampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    link = models.ForeignKey('links.Link', related_name='votes', on_delete=models.CASCADE)