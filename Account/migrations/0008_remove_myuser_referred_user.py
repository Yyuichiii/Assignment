# Generated by Django 5.0.4 on 2024-04-07 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_myuser_referred_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='referred_user',
        ),
    ]