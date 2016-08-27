from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from project.models import Project
from project.serializers import ProjectCreateSerializer
from project.services import ProjectService
from spider.scheduler.tasks import scheduling
from utils.helpers import base62_encode


class ProjectViewSet(viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        proj = serializer.save()
        sl = scheduling.delay(proj_id=base62_encode(proj.id),
                              links=[proj.entry_url],
                              options=ProjectService.gen_project_options(proj))
        # send_links = sl.get()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
