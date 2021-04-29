from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from uuid import uuid4

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    price = models.FloatField()
    status = models.CharField(
        max_length=2,
        choices = (
            ('C', 'Completo'),
            ('AP','Aguardando Pagamento'),
            ('P','Processando'),
            ('E','Enviado'),
            ('CN','Cancelado')
        )
    )
    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()




