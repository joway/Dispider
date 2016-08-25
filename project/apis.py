from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from project.serializers import ProjectCreateSerializer
from spider.scheduler import SchedulerService


class ProjectViewSet(viewsets.GenericViewSet):
    serializer_class = ProjectCreateSerializer
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.validated_data
        SchedulerService.scheduling_tasks(data['id'], [data['entry_url']])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
