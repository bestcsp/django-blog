# Generated by Django 3.0.1 on 2020-03-25 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100)),
                ('comment', models.TextField(max_length=300)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
