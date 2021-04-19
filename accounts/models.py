from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    cpf = models.PositiveBigIntegerField(max_length=11)
    address = models.CharField(max_length=50)
    house_number = models.CharField(max_length=30)
    address_complement = models.CharField(max_length=255)
    cep = models.PositiveIntegerField(max_length=8)
    def __str__(self):
        return self.user.username