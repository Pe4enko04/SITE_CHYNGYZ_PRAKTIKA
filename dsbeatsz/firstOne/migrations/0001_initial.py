# Generated by Django 4.2 on 2023-04-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chyngyz_Aitmatov', models.CharField(max_length=255)),
                ('year_of_brith', models.DateTimeField()),
                ('Year_of_death', models.DateTimeField(blank=True)),
                ('Biogarfia', models.TextField()),
                ('Detstvo_unost', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
