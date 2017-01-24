from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Articles(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)

    def __str__(self):
        return self.title



        





class Comments(models.Model):
    content = models.CharField(max_length=250)
    articles_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
    posted_time = models.DateTimeField(default=timezone.now)
    parent_id = models.IntegerField(db_index=True, default=0)
#    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

