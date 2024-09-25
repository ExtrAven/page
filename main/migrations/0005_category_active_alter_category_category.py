# Generated by Django 5.1.1 on 2024-09-25 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_category_image_alter_product_image_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('Hogar', 'Hogar'), ('Muebles', 'Muebles'), ('Electrodomésticos', 'Electrodomésticos'), ('Juguetes', 'Juguetes'), ('Videojuegos', 'Videojuegos'), ('Computación', 'Computación'), ('Accesorios', 'Accesorios')], default='General', max_length=50),
        ),
    ]
