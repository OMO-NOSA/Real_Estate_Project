# Generated by Django 2.1.5 on 2019-02-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='address',
            field=models.CharField(default='welcome', max_length=200),
        ),
    ]
