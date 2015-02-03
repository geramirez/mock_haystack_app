from django.shortcuts import render
# from haystack.query import SearchQuerySet
from mockapp.models import Request

# We can pass lower-level args into haystack
from elasticsearch import Elasticsearch
es = Elasticsearch()


def document_page(request, doc_id):
    """ Returns a document page """
    try:
        doc = Request.objects.get(doc_id=doc_id)
    except:
        # add a message later
        pass

    try:
        # We can pass lower-level args into haystack
        similar = es.mlt(
            index='haystack',
            id="mockapp.request.%s" % doc_id,
            doc_type='modelresult',
            percent_terms_to_match=.1)
        similar = [t['_source'] for t in similar['hits']['hits']]

        #similars = SearchQuerySet().more_like_this(doc)[0:10]

    except:
        similar = ""

    return render(
        request,
        "doc_page.html",
        {'doc': doc, 'similars': similar})
