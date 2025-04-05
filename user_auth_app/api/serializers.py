import random
from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from join_app.dummy_datas import contact_templates, task_templates
from join_app.models import UserContact, Task, Subtask

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
def create_contacts_for_user(user):
    contact_ids = []
    for contact_data in contact_templates:
        contact = UserContact.objects.create(
            user=user,
            color=contact_data['color'],
            email=contact_data['email'],
            name=contact_data['name'],
            phone=contact_data['phone'],
            shortcut=contact_data['shortcut']
        )
        contact_ids.append(contact.id)
    return contact_ids

def create_tasks_for_user(user, contact_ids):
    for task_data in task_templates:
        task = Task.objects.create(
            user=user,
            title=task_data['title'],
            description=task_data['description'],
            dueDate=task_data['dueDate'],  
            prio=task_data['priority'],     
            category=task_data['category'],
            status=task_data['status'],
            position=task_data['position']
        )

 
        num_contacts = random.randint(1, min(5, len(contact_ids)))  
        assigned_ids = random.sample(contact_ids, num_contacts)  
        assigned_contacts = UserContact.objects.filter(id__in=assigned_ids)

        task.assignTo.set(assigned_contacts)

        subtasks = task_data.get('subtasks', [])
        for subtask_data in subtasks:
            Subtask.objects.create(
                task=task,
                title=subtask_data['title'],
                complete=subtask_data['complete']
            )
      
class RegistrationSerializer(serializers.ModelSerializer):
    
    repeated_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields  = ['username', 'email', 'password', 'repeated_password', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        account = User(
            email=self.validated_data['email'], 
            username=self.validated_data['username'], 
            first_name=self.validated_data.get('first_name', ''), 
            last_name=self.validated_data.get('last_name', '')
        )
        account.set_password(self.validated_data['password'])
        account.save()
        
        full_name = f"{account.first_name} {account.last_name}".strip()
        shortcut = (account.first_name[:1] + account.last_name[:1]).upper()

        UserContact.objects.create(
            user=account,
            color='gold',
            phone='',
            email=account.email,
            name=f"{full_name} (Yourself)",
            shortcut=shortcut
        )
        
        contact_ids = create_contacts_for_user(account)
        create_tasks_for_user(account, contact_ids)
        
        return account
    
class LogInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({'email': 'Email does not exist'})
        user = authenticate(username=user.username, password=password)
        if user is None:
            raise serializers.ValidationError({'password': 'Wrong password'})
        
        data['user'] = user
        return data