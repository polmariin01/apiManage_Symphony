from django.db import models

# Create your models here.


class Symphony_Counting_Model(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=255)
    countedInteractions = models.IntegerField(default=0)
    isTrending = models.BooleanField(default=False)

    def __str__(self):
        return self.name + f' - {self.countedInteractions} requests'