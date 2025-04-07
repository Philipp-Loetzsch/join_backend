from rest_framework import serializers
from join_app.models import Task, Subtask, UserContact


class SubtaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Subtask model.

    Serializes/deserializes Subtask instances, including id, title, and complete status.
    """
    class Meta:
        model = Subtask
        fields = ['id', 'title', 'complete']


class UserContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserContact model.

    Serializes/deserializes UserContact instances, excluding the 'user' field.
    """
    class Meta:
        model = UserContact
        exclude = ['user']


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model, handling nested Subtasks and UserContact assignments.

    Serializes Task instances including nested Subtask objects. For writing operations,
    it accepts nested data for creating subtasks and a list of UserContact primary keys
    for assigning contacts.
    """
    subtasks = SubtaskSerializer(many=True, required=False)

    assignTo = UserContactSerializer(many=True, read_only=True)
    assignTo_ids = serializers.PrimaryKeyRelatedField(
        queryset=UserContact.objects.all(),
        many=True,
        write_only=True,
        source='assignTo',
        required=False
    )

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        """
        Creates a new Task instance along with its associated Subtasks and assignments.

        Args:
            validated_data (dict): Validated data received from the request, potentially
                                   including 'subtasks' (list of dicts) and 'assignTo'
                                   (list of UserContact instances derived from assignTo_ids).

        Returns:
            Task: The newly created Task instance.
        """
        subtasks_data = validated_data.pop('subtasks', [])
        assigned_contacts = validated_data.pop('assignTo', [])

        task = Task.objects.create(**validated_data)

        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)

        task.assignTo.set(assigned_contacts)

        return task

    def update(self, instance, validated_data):
        """
        Updates an existing Task instance, replaces its Subtasks, and updates assignments.

        Args:
            instance (Task): The existing Task instance to update.
            validated_data (dict): Validated data received from the request for update.
                                   May include 'subtasks' and 'assignTo' keys.

        Returns:
            Task: The updated Task instance.
        """
        subtasks_data = validated_data.pop('subtasks', None)
        assigned_contacts = validated_data.pop('assignTo', None)

        instance = super().update(instance, validated_data)

        if subtasks_data is not None:
            instance.subtasks.all().delete()
            for subtask_data in subtasks_data:
                Subtask.objects.create(task=instance, **subtask_data)

        if assigned_contacts is not None:
            instance.assignTo.set(assigned_contacts)

        return instance