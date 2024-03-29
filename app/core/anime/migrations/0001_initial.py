# Generated by Django 5.0 on 2023-12-31 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='animes/%Y/%m/%d', verbose_name='Picture')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'Anime',
                'verbose_name_plural': 'Anime',
                'db_table': 'Anime',
                'ordering': ['id'],
            },
        ),
    ]
