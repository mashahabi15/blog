# Generated by Django 2.2 on 2021-04-03 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_commententity_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commententity',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='commententity',
            name='like',
        ),
    ]
