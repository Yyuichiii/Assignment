# Generated by Django 5.0.4 on 2024-04-06 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='referral_code',
            field=models.CharField(blank=True, help_text='A unique referral code assigned to the user.', max_length=6, unique=True),
        ),
    ]
