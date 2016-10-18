# from article.models import Article
#
# data = Article.objects.filter(url__contains='www.seraph-fd.cn')
# print(len(data))
# for d in data:
#     d.delete()
from elastic.services import ElasticService
from utils.helpers import get_root_domain
url = 'http://www.seraph-fd.cn/'
ElasticService.delete(index='tech', doc_type=get_root_domain(url))
