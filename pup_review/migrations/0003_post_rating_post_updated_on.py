# Generated by Django 4.2.14 on 2024-08-14 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pup_review', '0002_post_status_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.IntegerField(choices=[(1, '1🐾'), (2, '2🐾'), (3, '3🐾'), (4, '4🐾'), (5, '5🐾')], default=None),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
