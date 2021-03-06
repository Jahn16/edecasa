# Generated by Django 3.2 on 2021-04-28 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fourth_image',
            field=models.ImageField(blank=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='second_image',
            field=models.ImageField(blank=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='third_image',
            field=models.ImageField(blank=True, upload_to='product_images'),
        ),
    ]
