# Generated by Django 2.2.1 on 2019-08-15 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20190813_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.TextField(max_length=120, null=True),
        ),
    ]
