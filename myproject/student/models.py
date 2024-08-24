from django.db import models
from college.models import College
 
class STUDENT(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_no = models.IntegerField()
    college_name = models.TextField()

    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name