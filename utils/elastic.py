from elasticsearch import Elasticsearch

from config.settings import ELASTIC_HOSTS

elatic = Elasticsearch(
    ELASTIC_HOSTS,
    http_auth=('user', 'secret'),
)
