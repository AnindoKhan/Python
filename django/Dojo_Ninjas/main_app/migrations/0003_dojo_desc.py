# Generated by Django 2.2.4 on 2020-11-06 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201105_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
