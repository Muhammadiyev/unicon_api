# Generated by Django 3.1.3 on 2020-11-24 17:03

from django.db import migrations
import taskapi.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taskapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draganddrop',
            name='position',
            field=taskapi.fields.OrderField(blank=True),
        ),
    ]
