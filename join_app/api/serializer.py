from rest_framework import serializers
from join_app.models import Task, Contact, Subtask, UserContact

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['user']

class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContact
        exclude = ['user', 'contact']

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, read_only=True)
    subtask_ids = serializers.PrimaryKeyRelatedField(
        queryset=Subtask.objects.all(),
        many=True,
        write_only=True,
        source='subtasks'
    )
    
    assignTo = ContactSerializer(many=True, read_only=True)
    assignTo_ids = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(),
        many=True,
        write_only=True,
        source='assignTo'
    )

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user'] 

