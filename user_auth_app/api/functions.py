from join_app.models import UserContact, Task, Subtask
from join_app.dummy_datas import contact_templates, task_templates
import random

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