# Generated by Django 5.0.6 on 2024-07-13 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_rename_id_post_comment_idpost_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='idpost',
            new_name='id_post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='iduser',
            new_name='id_user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='postid',
            new_name='post_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='userid',
            new_name='user_id',
        ),
    ]
