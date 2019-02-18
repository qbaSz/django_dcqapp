from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class DCEntry(models.Model):
    commit_id = models.CharField(max_length=50)
    change_id = models.CharField(max_length=50)
    author    = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date pushed')
    verified = models.BooleanField()

    def __str__(self):
        return self.commit_id + ' ' + self.author

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class DCAuthor(models.Model):
    author_name = models.CharField(max_length=50)
    dc_value = models.IntegerField(default=0)
    dc_entry = models.ForeignKey(DCEntry, on_delete=models.CASCADE)