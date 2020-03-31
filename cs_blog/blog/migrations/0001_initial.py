# Generated by Django 3.0.1 on 2020-03-22 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=300)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]