# Generated by Django 5.0.6 on 2024-07-11 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='joined_date',
            field=models.DateField(null=True),
        ),
    ]
