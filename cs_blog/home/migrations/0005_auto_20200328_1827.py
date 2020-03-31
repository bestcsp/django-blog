# Generated by Django 3.0.1 on 2020-03-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='age',
            field=models.IntegerField(default=20, max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]