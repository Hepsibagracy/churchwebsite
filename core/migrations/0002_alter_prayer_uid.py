# Generated by Django 5.0.2 on 2024-03-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayer',
            name='uid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]