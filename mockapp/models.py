from django.db import models


class Tweet(models.Model):
    pub_date = models.DateTimeField()
    from_user = models.CharField(max_length=100)
    message = models.TextField()

    def __unicode__(self):
        return self.message


class Post(models.Model):
    pub_date = models.DateTimeField()
    message = models.TextField()

    def __unicode__(self):
        return self.message
