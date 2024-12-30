from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contacts'  # user.contacts.all()
    )

    class Meta:
        unique_together = ('user', 'email')

    def __str__(self):
        return f"{self.name} <{self.email}>"