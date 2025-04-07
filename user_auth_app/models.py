from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    """
    Extends the standard Django User model using a one-to-one relationship.

    This model provides a way to associate additional profile information
    with a User, although currently it only holds the direct link.

    Attributes:
        user (OneToOneField to User): A one-to-one link to the corresponding
            Django User instance. If the User is deleted, this UserProfile
            will also be deleted due to `on_delete=models.CASCADE`.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns the username of the associated User."""
        return self.user.username