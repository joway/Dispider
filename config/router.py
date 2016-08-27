from rest_framework import routers

from project.apis import ProjectViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r"proj", ProjectViewSet, base_name="proj")
