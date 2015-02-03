from haystack import indexes
from mockapp.models import Request


class RequestIndex(indexes.SearchIndex, indexes.Indexable):

    doc_id = indexes.CharField(model_attr='doc_id')
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Request

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
