from django.db import models

# Create your models here.


class Blog(models.Model):
    request_place = models.CharField(max_length=20)
    meet_place = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    detail_request = models.TextField()
    fees = models.TextField()

    def __str__(self):
        return self.request_place
