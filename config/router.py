from rest_framework import routers

from article.apis import ArticleViewSet
from project.apis import ProjectViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r"proj", ProjectViewSet, base_name="proj")
router.register(r"article", ArticleViewSet, base_name="article")
