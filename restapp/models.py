from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False, default=uuid.uuid4())
    created_at = models.DateField(auto_created=True)
    updated_at = models.DateField(auto_created=True)


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

#crud--------
   
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    cover = models.CharField(max_length=50, null=True, blank=True)  # Optional
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.title



    