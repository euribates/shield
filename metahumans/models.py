from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


class Team(models.Model):
    '''Algunos superheroes o villanos se agrupan en equipos.
    '''
    name = models.CharField(max_length=100, unique=True)
    headquarter = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.name


class Power(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, unique=True)  # No puede haber nombres duplicados
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Identity(models.Model):
    first_name = models.CharField(max_length=130)
    last_name = models.CharField(max_length=270, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def up_to_one_hundred(value):
    if value > 100:
        raise ValidationError('El valor no puede exeder de 100')


class Metahuman(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    identity = models.OneToOneField(
        Identity,
        blank=True,
        null=True,
        related_name='alter_ego',
        on_delete=models.PROTECT,
        )
    level = models.PositiveIntegerField(
        default=1,
        validators=[
            up_to_one_hundred,
            ]
        )
    team = models.ForeignKey(
        Team,
        blank=True,
        null=True,
        related_name='components',
        on_delete=models.PROTECT,
    )
    powers = models.ManyToManyField(Power)
    is_active = models.BooleanField(default=True)
    photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='metahumans',
    )

    def is_dangerous(self):
        return self.level >= 50

    def __str__(self):
        return f"{self.name} [{self.level}]"

    def num_powers(self):
        return self.powers.count()
