from django.db import models
 
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_no = models.IntegerField()
    company_type = models.TextField()

    def __str__(self):
        return self.name 