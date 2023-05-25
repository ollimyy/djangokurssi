from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
