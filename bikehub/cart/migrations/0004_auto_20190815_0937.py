# Generated by Django 2.2.1 on 2019-08-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20190815_0638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Email',
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='niteshraz619@gmail.com', max_length=250, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.TextField(choices=[('Started', 'Started'), ('Abandoned', 'Abandoned'), ('Finished', 'Finished')], max_length=120, null=True),
        ),
    ]
