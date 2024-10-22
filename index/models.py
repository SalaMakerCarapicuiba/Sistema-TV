
from django.conf.urls.static import static
import uuid
from .utils  import CustomerTypes
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField
import datetime


# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    role = models.IntegerField(choices=CustomerTypes.choices(), default=CustomerTypes.USER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name}'

class Notices(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    sharing = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=20)
    category = models.CharField(max_length=30)
    subcategory = models.CharField(max_length=30)
    content = models.TextField(max_length=70)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    local = models.CharField(max_length=15)
    responsible = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    imagem = models.ImageField(upload_to='imgNoticias/', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
   

class Materia(models.Model):
    DIAS_DA_SEMANA = [
        (2, 'Segunda-feira'),
        (3, 'Terça-feira'),
        (4, 'Quarta-feira'),
        (5, 'Quinta-feira'),
        (6, 'Sexta-feira'),
        (7, 'Sábado'),
    ]

    nome = models.CharField(max_length=100)
    semestre = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    dia_da_semana = MultiSelectField(choices=DIAS_DA_SEMANA)
    professor = models.CharField(max_length=30)
    sala = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.nome}'


class Horario(models.Model):
    PERIODO = [
        (1, 'Matutino'),
        (2, 'Vespertino'),
        (3, 'Noturno'),
    ]

    horario_de_inicio = models.TimeField(null=True)
    horario_de_termino = models.TimeField(null=True)
    periodo = models.IntegerField(choices=PERIODO)

class Recados (models.Model):
    data_inicio = models.DateField()
    data_final = models.DateField()
    titulo = models.CharField(max_length=30)
    contexto = models.CharField(max_length=20)
    responsavel = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.titulo}'