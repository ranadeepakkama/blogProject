# Generated by Django 4.2 on 2023-05-16 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_created_at_alter_post_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
