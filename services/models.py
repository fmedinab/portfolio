from django.db import models
from django.db.models.fields import  CharField,URLField
from django.db.models.fields.files import ImageField
import uuid
import datetime


# Create your models here.
class Service(models.Model):
    id =models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    title = CharField(max_length=100)
    description = models.TextField()
    imagen = ImageField(null=True, blank=True,default="",upload_to='services/img/')
    url = URLField(blank=True)
    date = models.DateField(datetime.date.today)

    def __str__(self):
        return self.title
