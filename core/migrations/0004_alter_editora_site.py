# Generated by Django 5.0.2 on 2024-03-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_editora"),
    ]

    operations = [
        migrations.AlterField(
            model_name="editora",
            name="site",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
