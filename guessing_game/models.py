from django.db import models


# This model will store the randomly chosen number and the number of attempts made by the user.
class Game(models.Model):
    number = models.IntegerField()
    attempts = models.IntegerField(default=0)