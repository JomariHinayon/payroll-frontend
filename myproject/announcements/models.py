from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.ImageField(upload_to='announcements/')
    image2 = models.ImageField(upload_to='announcements/')
    image3 = models.ImageField(upload_to='announcements/')

    def __str__(self):
        return self.title

