# Generated by Django 2.2 on 2021-04-03 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210403_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commententity',
            name='parent_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.CommentEntity'),
        ),
    ]