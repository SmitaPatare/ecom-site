# Generated by Django 3.1.6 on 2021-02-17 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mobile_no', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('password', models.IntegerField()),
            ],
        ),
    ]
