# Generated by Django 5.0 on 2024-01-02 23:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anime', '0002_alter_anime_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('duration', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='static/chapter/%Y/%m/%d', verbose_name='Picture')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='anime.anime')),
            ],
            options={
                'verbose_name': 'chapter',
                'verbose_name_plural': 'chapters',
                'db_table': 'chapters',
                'ordering': ['id'],
            },
        ),
    ]
