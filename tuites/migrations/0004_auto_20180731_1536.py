# Generated by Django 2.0.7 on 2018-07-31 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tuites', '0003_auto_20180730_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuite',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]