# Generated by Django 5.1.1 on 2024-09-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_category_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Hogar', 'Hogar'), ('Muebles', 'Muebles')], default='General', max_length=50),
        ),
    ]
