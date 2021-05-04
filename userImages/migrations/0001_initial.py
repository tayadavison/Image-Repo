# Generated by Django 3.2 on 2021-05-04 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pictures')),
                ('title', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
            ],
        ),
    ]
