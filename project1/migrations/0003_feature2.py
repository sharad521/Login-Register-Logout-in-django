# Generated by Django 3.2.9 on 2021-11-22 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0002_feature1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=500)),
            ],
        ),
    ]
