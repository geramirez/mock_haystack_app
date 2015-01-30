from elasticsearch import Elasticsearch
es = Elasticsearch()


q = {
    "query": {
        "bool": {
            "must": [
                {"match": {"text": "obama"}},
                {"match": {"text": "kerry"}}
            ]
        }
    }
}

res = es.search(index="haystack", body=q)
#print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    #print("%(id)s: %(text)s" % hit["_source"])

    similar = es.mlt(
        index='haystack',
        id=hit['_source']['id'],
        doc_type='modelresult',
        percent_terms_to_match=.1)
    if similar['hits']['total'] > 0:
        print(similar['hits']['hits'][0]['_source'])
