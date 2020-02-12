from django.db import models

# Create your models here.


class APIKey(models.Model):

    api_key = models.CharField(max_length=128, primary_key=True, unique=True)
    exhausted = models.BooleanField(default=False)

    def __str__(self):
        return "Exhausted: %s, %s" % (str(self.exhausted), self.api_key)

