from django.contrib.auth.models import User
from django.db.models import Model, CharField, ForeignKey, CASCADE, TextField, BooleanField, DateTimeField


class Task(Model):
    user = ForeignKey(User, CASCADE, null=True, blank=True)
    title = CharField(max_length=255)
    description = TextField(null=True, blank=True)
    complete = BooleanField(default=False)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('complete',)
