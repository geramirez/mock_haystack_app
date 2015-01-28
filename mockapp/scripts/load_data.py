import csv
from mockapp.models import Tweet
from mockapp.settings import BASE_DIR


with open(BASE_DIR + '/mockapp/scripts/twitter_bank.csv', 'r') as csvfile:
    csvfile.readline()

    tweets = csv.reader(csvfile)
    for row in tweets:
        try:
            t = Tweet(
                pub_date='2015-01-01 01:00', message=row[5], from_user=row[15])
            t.save()
        except:
            print("fail")
