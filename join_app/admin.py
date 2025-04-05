# from django.contrib import admin
# from .models import Task, Subtask, UserContact

# # Register your models here.
# admin.site.register(UserContact)
# admin.site.register(Task)
# admin.site.register(Subtask)


from django.contrib import admin
from .models import Task, Subtask, UserContact

# Dynamische Admin-Klasse, die alle Felder inklusive 'id' anzeigt
class DynamicAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = ['id'] + [field.name for field in model._meta.fields if field.name != 'id']
        super().__init__(model, admin_site)

# Registrierung mit der dynamischen Admin-Klasse
admin.site.register(UserContact, DynamicAdmin)
admin.site.register(Task, DynamicAdmin)
admin.site.register(Subtask, DynamicAdmin)
