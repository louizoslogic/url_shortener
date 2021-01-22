from django.db import models


class Url(models.Model):

    direct = models.CharField(max_length=200)
    hashed = models.CharField(max_length=200)
    counter = models.IntegerField(default=1)

    def __str__(self):
        return self.direct
