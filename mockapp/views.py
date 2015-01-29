from django.shortcuts import render
from mockapp.models import Tweet


def document_page(request, postid):
    """ Returns a document page """
    try:
        doc = Tweet.objects.filter(postid=postid).values()[0]
        print(doc)
    except:
        doc = {"error": "Could not find a tweet"}

    return render(request, "doc_page.html", {'doc': doc, 'similars': []})
