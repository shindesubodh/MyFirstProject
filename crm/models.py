from django.db import models
# Create your models here.

class task (models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)


class Review (models.Model):

    reviewer_name = models.CharField(max_length=50) 
    review_title = models.CharField (max_length=50)
    task = models.ForeignKey (task, on_delete=models.CASCADE)

