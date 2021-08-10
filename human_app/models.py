from django.db import models

# Create your models here.

#model to store Image in database
class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="media")
    def __str__(self):
        # return self.image
        return self.caption
