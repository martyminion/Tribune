# Generated by Django 3.0.6 on 2020-05-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='no image set', upload_to='articles/'),
            preserve_default=False,
        ),
    ]
