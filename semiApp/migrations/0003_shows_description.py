# Generated by Django 2.2.4 on 2021-03-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semiApp', '0002_remove_shows_actions'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='Description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]