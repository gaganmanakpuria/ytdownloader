# Generated by Django 3.0.3 on 2020-04-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yapp', '0002_auto_20200418_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('av', models.FileField(upload_to='')),
            ],
        ),
    ]
