# Generated by Django 5.0.2 on 2024-02-08 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story_management',
            options={'ordering': ['-createdAt', '-updatedAt']},
        ),
    ]
