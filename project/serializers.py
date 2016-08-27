from rest_framework import serializers

from project.models import Project


class ProjectOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('rules', 'payload', 'process_type', 'http_method', 'headers', 'cookies')


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'entry_url', 'rules')


class ProjectCallbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('proj_id', 'task_id', 'links', 'status')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
