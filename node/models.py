from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Node(models.Model):
    title = models.CharField(max_length=400)
    content = models.TextField()
    topic = models.CharField(max_length=300)
    file = models.URLField(max_length=500, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('node-detail', kwargs={'pk': self.pk})
