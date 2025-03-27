from django.db import models
from users.models import CustomUser
from adminpanel.models import App

class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/')
    completed = models.BooleanField(default=False)

class Submission(models.Model):
    task = models.ForeignKey("Task", on_delete=models.CASCADE)
    user = models.ForeignKey("users.UserProfile", on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to="submissions/")
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("approved", "Approved"), ("rejected", "Rejected")])

    def __str__(self):
        return f"{self.user} - {self.task} - {self.status}"
