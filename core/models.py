from django.db import models
import uuid
# Create your models here.


class Prayer(models.Model):
    uid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=60)
    pemail=models.EmailField(max_length=100)
    pphone=models.CharField(max_length=10)
    pmessage=models.TextField(max_length=1000)

class Contact(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=60)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=10)
    subject=models.CharField(max_length=200)
    message=models.TextField(max_length=1000)

    def __str__(self):
        return f"contact {self.name}"
    



