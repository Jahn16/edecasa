from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from utils import validate


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    cpf = models.PositiveBigIntegerField()
    address = models.CharField(max_length=50)
    house_number = models.CharField(max_length=30)
    address_complement = models.CharField(max_length=255)
    cep = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username

    def clean(self):
        error_messages = {}
        if not validate.validate_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido.'
        if not validate.validate_cep(self.cep):
            error_messages['cep'] = 'Digite um CEP válido.'
        if error_messages:
            raise ValidationError(error_messages)

