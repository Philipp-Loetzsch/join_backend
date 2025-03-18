# from rest_framework import serializers
# from join_app.models import Task, Subtask, UserContact

# class SubtaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subtask
#         fields = ['id', 'title', 'complete']


# class UserContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserContact
#         exclude = ['user']

# class TaskSerializer(serializers.ModelSerializer):
#     subtasks = SubtaskSerializer(many=True, read_only=True)
#     subtask_ids = serializers.PrimaryKeyRelatedField(
#         queryset=Subtask.objects.all(),
#         many=True,
#         write_only=True,
#         source='subtasks'
#     )
    
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

class TaskSerializer(serializers.ModelSerializer):
    # Für die Anzeige der vorhandenen Subtasks
    subtasks = SubtaskSerializer(many=True, read_only=True)
    # Für das Erstellen von Subtasks
    subtasks_data = SubtaskSerializer(many=True, write_only=True, required=False)
    
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
        # Extrahiere die Subtask-Daten (falls vorhanden)
        subtasks_data = validated_data.pop('subtasks_data', [])
        # Erstelle den Task
        task = Task.objects.create(**validated_data)
        # Erstelle die Subtasks und verknüpfe sie mit dem Task
        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)
        # Damit die Rückbeziehung (reverse relation) aktualisiert wird:
        task.refresh_from_db()
        return task


