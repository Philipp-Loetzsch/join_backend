from rest_framework import serializers
from join_app.models import Task, Subtask, UserContact


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'

class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContact
        exclude = ['user']

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, read_only=True)
    subtask_ids = serializers.PrimaryKeyRelatedField(
        queryset=Subtask.objects.all(),
        many=True,
        write_only=True,
        source='subtasks'
    )
    
    assignTo = UserContactSerializer(many=True, read_only=True)
    assignTo_ids = serializers.PrimaryKeyRelatedField(
        queryset=UserContact.objects.all(),
        many=True,
        write_only=True,
        source='assignTo'
    )

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user'] 

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'
        read_only_fields = ['task']