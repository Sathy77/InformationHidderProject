# Generated by Django 2.2 on 2020-10-15 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Encode', '0006_remove_encodeddata_hiddenimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encodeddata',
            name='DataImage',
        ),
        migrations.AddField(
            model_name='encodeddata',
            name='SavingPath',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
