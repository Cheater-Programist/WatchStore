# Generated by Django 5.1 on 2024-08-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_age',
            field=models.IntegerField(default=1, verbose_name='Возраст'),
            preserve_default=False,
        ),
    ]
