# Generated by Django 2.2 on 2021-04-03 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20210403_0728'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_type', models.IntegerField(blank=True, choices=[(1, 'like'), (2, 'dislike')], default=None)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_trends', to='blog.CommentEntity')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_trends', to='blog.PostEntity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_trends', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'trend_entities',
                'db_table': 'trend_entity',
            },
        ),
    ]