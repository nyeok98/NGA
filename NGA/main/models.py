from django.db import models

# Create your models here.


class Blog(models.Model):
    request_place = models.CharField(max_length=20)
    meet_place = models.CharField(max_length=20)
    pub_date = models.DateTimeField('auto_now_add=True')
    detail_request = models.TextField()
    fees = models.TextField()
    limited_time_hour = models.IntegerField('number', default=0)
    limited_time_min = models.IntegerField('number', default=0)
    limited_time_sec = models.IntegerField('number', default=0)

    def __str__(self):
        return self.request_place
