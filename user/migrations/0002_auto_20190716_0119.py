# Generated by Django 2.2.3 on 2019-07-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='nickname',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
