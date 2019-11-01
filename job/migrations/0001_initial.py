# Generated by Django 2.2.6 on 2019-11-01 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=500, null=True)),
                ('intro', models.CharField(max_length=3000, null=True)),
                ('main_tasks', models.CharField(max_length=3000, null=True)),
                ('requirements', models.CharField(max_length=3000, null=True)),
                ('preferred_points', models.CharField(max_length=3000, null=True)),
                ('benefits', models.CharField(max_length=3000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Categories')),
                ('companise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Companise')),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
    ]
