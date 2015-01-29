from django.db import models


class Tweet(models.Model):
    """ Model to store tweets """
    postid = models.CharField(max_length=40, primary_key=True)
    created_time = models.DateTimeField()
    from_user = models.CharField(max_length=100)
    retweeted_from = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    retweets = models.IntegerField()
    favorites = models.IntegerField()

    def __unicode__(self):
        return self.message
