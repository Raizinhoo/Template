# Generated by Django 5.0.2 on 2024-03-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_autor"),
    ]

    operations = [
        migrations.AddField(
            model_name="autor",
            name="nome",
            field=models.CharField(default="Autor", max_length=100),
        ),
    ]
