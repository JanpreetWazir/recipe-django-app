# Generated by Django 5.1.4 on 2024-12-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(max_length=50)),
                ('receipe_description', models.CharField(max_length=200)),
                ('receipe_image', models.ImageField(upload_to='receipe')),
            ],
        ),
    ]
