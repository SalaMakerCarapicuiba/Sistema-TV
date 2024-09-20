
from django.conf.urls.static import static
import uuid
from .utils  import CustomerTypes
from django.db import models


# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    role = models.IntegerField(choices=CustomerTypes.choices(), default=CustomerTypes.USER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Notices(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    sharing = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    content = models.TextField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    local = models.CharField(max_length=100)
    responsible = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imgNoticias/', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'