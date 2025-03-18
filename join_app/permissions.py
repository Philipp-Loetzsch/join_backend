from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    """Stellt sicher, dass nur der Besitzer eines Objekts darauf zugreifen kann"""

    def has_object_permission(self, request, view, obj):
        """Prüft, ob der angemeldete User der Besitzer des Objekts ist"""
        if hasattr(obj, "user"):  
            return obj.user == request.user  # Für Task und UserContact

        if hasattr(obj, "task"):  
            return obj.task.user == request.user  # Für Subtask

        return False  # Falls nichts passt, verweigern

