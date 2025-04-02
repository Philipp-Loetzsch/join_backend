from rest_framework import serializers
from join_app.models import Task, Subtask, UserContact

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'title', 'complete']

class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContact
        exclude = ['user']

# class TaskSerializer(serializers.ModelSerializer):

#     subtasks = SubtaskSerializer(many=True, read_only=True)
  
#     subtasks_data = SubtaskSerializer(many=True, write_only=True, required=False, source='subtasks')
    
#     assignTo = UserContactSerializer(many=True, read_only=True)
#     assignTo_ids = serializers.PrimaryKeyRelatedField(
#         queryset=UserContact.objects.all(),
#         many=True,
#         write_only=True,
#         source='assignTo'
#     )

#     class Meta:
#         model = Task
#         fields = '__all__'
#         read_only_fields = ['user']

#     def create(self, validated_data):
#         subtasks_data = validated_data.pop('subtasks', [])
#         assignTo_ids = validated_data.pop('assignTo', [])
              
#         task = Task.objects.create(**validated_data)
        
#         for subtask_data in subtasks_data:
#             Subtask.objects.create(task=task, **subtask_data)
            
#         task.assignTo.set(assignTo_ids)
     
#         task.refresh_from_db()
#         return task


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True)

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

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])  # Direkt aus subtasks extrahieren
        assignTo_ids = validated_data.pop('assignTo', [])

        task = Task.objects.create(**validated_data)

        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)

        task.assignTo.set(assignTo_ids)

        return task

    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        assignTo_ids = validated_data.pop('assignTo', [])

        # Bestehende Felder aktualisieren
        instance = super().update(instance, validated_data)

        # Alte Subtasks löschen und neue hinzufügen (alternativ: updaten statt löschen)
        instance.subtasks.all().delete()
        for subtask_data in subtasks_data:
            Subtask.objects.create(task=instance, **subtask_data)

        instance.assignTo.set(assignTo_ids)

        return instance
