# Generated by Django 2.2.6 on 2019-10-31 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20191031_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companise',
            name='logo_img',
        ),
        migrations.RemoveField(
            model_name='companise',
            name='main_img',
        ),
        migrations.AddField(
            model_name='companise',
            name='logo_image',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='companise',
            name='main_image',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]
