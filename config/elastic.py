from elasticsearch import Elasticsearch

elatic = Elasticsearch(
    ['localhost'],
    http_auth=('user', 'secret'),
)
