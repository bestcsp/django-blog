# Generated by Django 3.0.1 on 2020-03-21 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=20)),
                ('content', models.TextField(max_length=300)),
            ],
        ),
    ]
