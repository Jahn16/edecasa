# Generated by Django 3.2 on 2021-04-17 19:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210417_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
