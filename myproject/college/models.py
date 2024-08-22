from django.db import models
 
class College(models.Model):
    collage_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_no = models.IntegerField()

    def __str__(self):
        return self.collage_name


