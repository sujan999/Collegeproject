# Generated by Django 2.2.1 on 2019-06-13 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_bike', models.IntegerField()),
                ('id_user', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='cart/')),
                ('date', models.DateTimeField()),
                ('content', models.TextField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='content',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='cart/')),
                ('date', models.DateTimeField()),
                ('status', models.TextField(default='pending')),
                ('bike_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cartid1', to='cart.Bike')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cartuser1', to='cart.Bike')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='bike_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cartid', to='cart.Bike'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cartuser', to='cart.Bike'),
        ),
    ]
