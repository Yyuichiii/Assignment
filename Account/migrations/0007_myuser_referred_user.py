# Generated by Django 5.0.4 on 2024-04-07 12:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_remove_myuser_referred_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='referred_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
