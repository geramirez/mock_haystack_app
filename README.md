# Notes on setting up elasticsearch
references:
[Installing Search Engines](http://django-haystack.readthedocs.org/en/latest/installing_search_engines.html)
[Haystack Setup Tutorial](http://django-haystack.readthedocs.org/en/latest/tutorial.html)

###Outline

#### Elasticsearch server
1. Installing
2. Setting up ES (mac)
3. Starting elasticsearch server

#### Haystack
1. Installing haystack and dependencies
2. connecting haystack to elasticsearch server
3. connecting models to search index
4. preparing data template
5. preparing frontend template
6. Indexing models

## Elasticsearch server
#### Installation
```bash
# Java is a dependency 
brew install Caskroom/cask/java
brew install elasticsearch
```

#### Setup
Elasticsearch requires a yaml config file. For more details on the config variables here you can visit the [documentation](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/setup-configuration.html). Below is sample file I used for running it locally. 

elasticsearch.yml
```yml
# Unicast Discovery (disable multicast)
discovery.zen.ping.multicast.enabled: false
discovery.zen.ping.unicast.hosts: ["127.0.0.1"]
cluster:
  name: mockes

network:
  host: 127.0.0.1

path:
  logs: /usr/local/var/log
  data: /usr/local/var/data
```

#### Starting Elasticsearch Server
`elasticsearch -f -D es.config=<path to YAML config>`

## Haystack
#### Installing haystack and dependencies
```bash
pip install elasticsearch
pip install django-haystack
```

#### Place ‘haystack’ into the INSTALLED_APPS list


#### Connecting haystack to elasticsearch server
In the settings create a variable called HAYSTACK_CONNECTIONS, it will contain the settings for connecting the django app to elasticsearch

```python
# Sample code
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
```

#### Connecting  models to search index
Haystack users SearchIndex objects to funnel data into elasticsearch. These objects are similar to django models or forms. 

Below is an example Model and SearchIndex

```python
# models.py
from django.db import models


class Tweet(models.Model):
    pub_date = models.DateTimeField()
    from_user = models.CharField(max_length=100)
    message = models.TextField()

    def __unicode__(self):
        return self.message
```

```
# search_indexes.py
import datetime
from haystack import indexes
from mockapp.models import Tweet


class TweetIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    author = indexes.CharField(model_attr='from_user')

    def get_model(self):
        return Tweet

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.order_by('author')
```


##### Notes: 
`document=True` indicates the primary field used to search. 
`use_template=True` sets indexing to use a data template when building the document the search engine will index.
`author` and `pub_date` are optional, but they allow additional filtering 
`index_queryset` allows additional filtering and sorting before the results are rendered. The objects here are related to the original model not the searchindex. 

#### Preparing the Data Template
Haystack uses templates to create the documents for haystack to index. You can place whatever fields you want haystack to index in these templates. For example, one template can contain multiple text fields like `title`, `body`, `author`, and `abstract`. 

It is important that these data templates are placed in the correct location within the app, because haystack is programmed to find them in specific dirs. The following example was placed in: `/templates/search/indexes/appname/tweet_text.txt`

```html
<!-- tweet_text.txt __>
{{ object.from_user }}
{{ object.message }}
```

#### Preparing Frontend Template
After the documents are index they will need to be rendered. Haystack already has pre-built urls with paging for django. 

- place the path below in the urls.py file
`(r'^search/', include('haystack.urls')),`

Also, a simple frontend template (like this one) can be places in the default location user “templates/search/search.html”

##### Indexing models
To start indexing use the rebuild_index commmand :
`python manage.py rebuild_index`
