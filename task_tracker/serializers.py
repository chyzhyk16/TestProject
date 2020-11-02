from rest_framework import serializers

from .models import Task, Board


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    creation_date = serializers.DateField()
    modification_date = serializers.DateField()
    execution_status = serializers.BooleanField()
    description = serializers.CharField()
    board_id = serializers.IntegerField()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.execution_status = validated_data.get('execution_status', instance.execution_status)
        instance.save()
        return instance


class BoardSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    creation_date = serializers.DateField()
    modification_date = serializers.DateField()

    def create(self, validated_data):
        return Board.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance