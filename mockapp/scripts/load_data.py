import csv
import datetime
from django.utils.timezone import utc
from mockapp.models import Tweet
from mockapp.settings import BASE_DIR


def load_data():
    with open(BASE_DIR + '/mockapp/scripts/twitter_bank.csv', 'r') as csvfile:

        csvfile.readline()
        tweets = csv.reader(csvfile)

        for row in tweets:
            created_time = datetime.datetime.strptime(
                row[6], "%a %b %d %H:%M:%S +0000 %Y")
            created_time = created_time.replace(tzinfo=utc)

            t = Tweet(
                postid=row[18][1:],
                created_time=created_time,
                from_user=row[15],
                message=row[5],
                retweets=row[11],
                favorites=row[19])
            t.save()
