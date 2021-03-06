# Generated by Django 3.2.6 on 2021-08-19 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0006_auto_20210817_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(default='exit', upload_to='album_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musician',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
