from django.db import models


class Url(models.Model):
    url = models.URLField()
    shorten_url = models.URLField()

    def __str__(self):
        return self.shorten_url
