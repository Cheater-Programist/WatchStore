# Generated by Django 5.1 on 2024-08-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Возраст'),
        ),
    ]
