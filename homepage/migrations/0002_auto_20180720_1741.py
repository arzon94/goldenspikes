# Generated by Django 2.0.7 on 2018-07-20 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='links',
            new_name='link1',
        ),
        migrations.AddField(
            model_name='submission',
            name='link2',
            field=models.URLField(default='http://2017-components-demo.cdn.byu.edu/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='link3',
            field=models.URLField(default='http://2017-components-demo.cdn.byu.edu/'),
            preserve_default=False,
        ),
    ]
