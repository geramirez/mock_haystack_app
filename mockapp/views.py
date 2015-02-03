from django.shortcuts import render
# from haystack.query import SearchQuerySet
from mockapp.models import Tweet

# We can pass lower-level args into haystack
from elasticsearch import Elasticsearch
es = Elasticsearch()


def document_page(request, postid):
    """ Returns a document page """
    try:
        doc = Tweet.objects.get(postid=postid)
    except:
        # add a message later
        pass

    try:
        # We can pass lower-level args into haystack
        similar = es.mlt(
            index='haystack',
            id="mockapp.tweet.%s" % postid,
            doc_type='modelresult',
            percent_terms_to_match=.1)
        similar = [t['_source'] for t in similar['hits']['hits']]

        # similars = SearchQuerySet().more_like_this(doc)[0:10]

    except:
        # add a message later
        pass

    print(similar)

    return render(
        request,
        "doc_page.html",
        {'doc': doc, 'similars': similar})
