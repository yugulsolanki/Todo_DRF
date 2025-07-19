from django.db import models

class Todo(models.Model):
    # id = models.AutoField()
    task = models.CharField(max_length = 30)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = "todo"

    def __str__(self):
        return self.task + self.completed