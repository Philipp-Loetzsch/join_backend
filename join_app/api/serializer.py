from rest_framework import serializers
from join_app.models import User, Task, Contact, Subtask

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'
class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, read_only=True)
    subtask_ids = serializers.PrimaryKeyRelatedField(
        queryset = Subtask.objects.all(),
        many=True,
        write_only=True,
        source='subtasks'
    )
    
    assignTo = ContactSerializer(many=True, read_only=True)
    assigntTo_ids = serializers.PrimaryKeyRelatedField(
        queryset = Contact.objects.all(),
        many=True,
        write_only=True,
        source='contacts'
    )
    class Meta:
        model = Task
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # tasks = TaskSerializer(many=True, read_only=True)
    # contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['name']
