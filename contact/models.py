from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return (
            self.title + " " + self.first_name + " " + self.last_name + ", " +
            self.email + " " + self.content + " " + "#" + self.location)
