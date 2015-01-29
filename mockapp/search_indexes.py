from haystack import indexes
from mockapp.models import Tweet


class TweetIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    created_time = indexes.DateTimeField(model_attr='created_time')
    author = indexes.CharField(model_attr='from_user')

    def get_model(self):
        return Tweet

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
