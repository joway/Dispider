from rest_framework import serializers

from spider.scheduler import Project


class ProjectOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('rules', 'payload', 'process_type', 'method', 'headers', 'cookies')


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'entry_url')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
