# Generated by Django 4.2 on 2024-02-06 12:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                ("name", models.CharField(max_length=50)),
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
