# Generated by Django 4.2.5 on 2023-09-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='pics')),
                ('note', models.TextField()),
            ],
        ),
    ]
