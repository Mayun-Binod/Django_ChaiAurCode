# Generated by Django 5.1.1 on 2024-10-01 17:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='chais/')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('ML', 'MASALA'), ('GR', 'GINGER'), ('KL', 'KIWI'), ('PL', 'PLAIN'), ('EL', 'ELACHI')], max_length=2)),
            ],
        ),
    ]
