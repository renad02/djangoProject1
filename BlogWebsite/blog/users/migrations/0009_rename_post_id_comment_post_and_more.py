# Generated by Django 5.0.6 on 2024-07-12 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_post_id_post_remove_user_id_unique_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_iD',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_iD',
            new_name='user',
        ),
    ]
