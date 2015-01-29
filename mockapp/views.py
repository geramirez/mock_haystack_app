from django.shortcuts import render
from haystack.query import SearchQuerySet
from mockapp.models import Tweet


def document_page(request, postid):
    """ Returns a document page """
    try:
        doc = Tweet.objects.get(postid=postid)
    except:
        # add a message later
        pass

    try:
        similars = SearchQuerySet().more_like_this(doc)[0:10]
    except:
        # add a message later
        pass

    return render(
        request,
        "doc_page.html",
        {'doc': doc, 'similars': similars})
