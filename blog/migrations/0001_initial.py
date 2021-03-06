# Generated by Django 3.2.8 on 2021-10-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True)),
                ('date', models.DateField()),
                ('content', models.TextField()),
            ],
        ),
    ]
